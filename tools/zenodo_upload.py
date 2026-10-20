#!/usr/bin/env python3
"""
Create Zenodo records for every document in the manifest.

    python tools/zenodo_manifest.py > zenodo.json
    python tools/zenodo_upload.py --sandbox        # rehearse
    python tools/zenodo_upload.py                  # create real drafts
    python tools/zenodo_upload.py --publish        # mint the DOIs

Uses Zenodo's InvenioRDM API (`/api/records`), not the legacy deposit API.
The legacy one has no creator type and no publisher field, so it files an
imprint as a person -- DataCite comes back with
`"nameType": "Personal", "familyName": "Wisdom Hill Research"` -- and stamps
the publisher as Zenodo. Both were seen on the sandbox before this was
rewritten.

Drafts by default. Publishing is the irreversible step -- a published Zenodo
record cannot be deleted, only superseded -- so it needs the explicit flag,
and the script asks before doing it.

Progress is kept in a state file (`zenodo-state.json`, or
`zenodo-state-sandbox.json`), keyed by the document's URL, so a re-run resumes
rather than duplicating. Delete the state file only if you have also deleted
the drafts it names.

The token is read from a file or the environment, and is never written to the
state file, printed, or put on a command line.
"""
import argparse, io, json, os, sys, time
import requests

TIMEOUT = 120


def api(base, token, method, path, **kw):
    url = path if path.startswith("http") else base + path
    # Pop once: on a retry the caller's Content-Type must still be there.
    headers = dict(kw.pop("headers", {}))
    headers["Authorization"] = "Bearer " + token
    if "json" in kw:
        headers.setdefault("Content-Type", "application/json")
    for attempt in range(4):
        r = requests.request(method, url, timeout=TIMEOUT,
                             headers=headers, **kw)
        if r.status_code not in (429, 500, 502, 503, 504):
            break
        wait = 2 ** attempt
        print("    %s %s -- retrying in %ds" % (r.status_code, r.reason, wait))
        time.sleep(wait)
    if not r.ok:
        sys.exit("%s %s failed: %s %s\n%s" % (method, url, r.status_code,
                                              r.reason, r.text[:600]))
    return r.json() if r.content else {}


RDM = {"Accept": "application/vnd.inveniordm.v1+json"}


def draft_doi(base, token, rid):
    """The DOI currently reserved on a draft, or None.

    Asked for explicitly: these endpoints answer in the legacy shape unless
    the InvenioRDM serializer is requested, and the legacy shape has no pids.
    """
    d = api(base, token, "GET", "/records/%s/draft" % rid, headers=dict(RDM))
    return ((d.get("pids") or {}).get("doi") or {}).get("identifier")


def reserve_doi(base, token, rid):
    """Reserve a DOI, or return the one the draft already has."""
    doi = draft_doi(base, token, rid)
    if doi:
        return doi
    api(base, token, "POST", "/records/%s/draft/pids/doi" % rid)
    doi = draft_doi(base, token, rid)
    if not doi:
        sys.exit("reserved a DOI for draft %s but cannot read it back" % rid)
    return doi


def load(path):
    return json.load(io.open(path, encoding="utf-8")) if os.path.exists(path) else {}


def save(path, state):
    io.open(path, "w", encoding="utf-8", newline="\n").write(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n")


def read_token(sandbox):
    """Find the access token without ever putting it on a command line.

    A token file is the simpler route on Windows: `setx` writes to the
    registry, and a program that is already running -- including whatever
    launched this shell -- keeps the environment it started with, so a freshly
    set variable is invisible until that program restarts. A file is read at
    the moment it is needed, and is scoped to this directory rather than to
    every process the account runs.

    Sandbox and production are separate Zenodo accounts with separate tokens,
    so they get separate files.
    """
    names = (["ZENODO_SANDBOX_TOKEN", "ZENODO_TOKEN"] if sandbox
             else ["ZENODO_TOKEN"])
    for n in names:
        if os.environ.get(n):
            return os.environ[n].strip()

    path = ".zenodo-token-sandbox" if sandbox else ".zenodo-token"
    if os.path.exists(path):
        token = io.open(path, encoding="utf-8").read().strip()
        if token:
            return token
        sys.exit("%s is empty" % path)

    nl = chr(10)
    sys.exit(
        "no access token." + nl +
        "  Put it in %s (one line, nothing else), or set %s." % (path, names[0]) + nl +
        "  Zenodo > top-right menu > Applications > Personal access tokens," + nl +
        "  with the scopes deposit:write and deposit:actions." + nl +
        "  " + ("Sandbox is a separate site with its own account and token."
               if sandbox else
               "This token can publish; keep the file out of version control."))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--manifest", default="zenodo.json")
    p.add_argument("--sandbox", action="store_true",
                   help="use sandbox.zenodo.org; separate account and token")
    p.add_argument("--reserve", action="store_true",
                   help="create the drafts and reserve their DOIs, then stop; "
                        "run tools/zenodo_doi_writeback.py and re-render before "
                        "uploading, so each PDF carries its own DOI")
    p.add_argument("--publish", action="store_true",
                   help="publish the drafts; this mints DOIs and cannot be undone")
    p.add_argument("--only", type=int, action="append",
                   help="restrict to these series positions (0 = Prologue, 15 = Epilogue)")
    args = p.parse_args()

    token = read_token(args.sandbox)

    base = ("https://sandbox.zenodo.org" if args.sandbox else "https://zenodo.org") + "/api"
    state_path = "zenodo-state-sandbox.json" if args.sandbox else "zenodo-state.json"
    state = load(state_path)

    records = json.load(io.open(args.manifest, encoding="utf-8"))
    if args.only:
        records = [r for r in records if r["order"] in args.only]

    if args.publish:
        pending = [r for r in records
                   if not state.get(r["url"], {}).get("doi")]
        print("About to PUBLISH %d record(s) on %s." % (len(pending), base))
        print("A published Zenodo record cannot be deleted. Type 'publish' to go on: ",
              end="", flush=True)
        if sys.stdin.readline().strip() != "publish":
            sys.exit("stopped; nothing was published")

    for rec in records:
        key, meta = rec["url"], rec["metadata"]
        here = state.setdefault(key, {})
        label = "[%2s] %s" % (rec["order"], meta["title"][:52])

        if here.get("doi"):
            print("%s  already published: %s" % (label, here["doi"]))
            continue

        if not args.reserve and not os.path.exists(rec["pdf"]):
            sys.exit("%s" % label + chr(10) +
                     "    missing %s -- run `quarto render` first" % rec["pdf"])

        body = {"access": {"record": "public", "files": "public"},
                "files": {"enabled": True},
                "metadata": meta}

        if not here.get("id"):
            d = api(base, token, "POST", "/records", json=body)
            here["id"] = d["id"]
            here["draft"] = d["links"].get("self_html")
            save(state_path, state)
            print("%s  draft %s" % (label, here["id"]))
        else:
            api(base, token, "PUT", "/records/%s/draft" % here["id"], json=body)

        if not here.get("reserved"):
            here["reserved"] = reserve_doi(base, token, here["id"])
            save(state_path, state)
            print("       reserved %s" % here["reserved"])

        if args.reserve:
            continue

        name = os.path.basename(rec["pdf"])
        if not here.get("file"):
            # Three steps: declare the name, send the bytes, commit.
            api(base, token, "POST", "/records/%s/draft/files" % here["id"],
                json=[{"key": name}])
            with io.open(rec["pdf"], "rb") as fh:
                api(base, token, "PUT",
                    "/records/%s/draft/files/%s/content" % (here["id"], name),
                    data=fh,
                    headers={"Content-Type": "application/octet-stream"})
            api(base, token, "POST",
                "/records/%s/draft/files/%s/commit" % (here["id"], name))
            here["file"] = name
            save(state_path, state)
            print("       uploaded %s" % name)

        if args.publish:
            out = api(base, token, "POST",
                      "/records/%s/draft/actions/publish" % here["id"])
            here["doi"] = (out.get("pids", {}).get("doi", {}).get("identifier")
                           or out.get("doi"))
            here["record"] = out.get("links", {}).get("self_html")
            save(state_path, state)
            print("       published %s" % here["doi"])

    done = sum(1 for v in state.values() if v.get("doi"))
    print("\n%d of %d published. State in %s."
          % (done, len(records), state_path))
    if args.reserve:
        print("DOIs are reserved and nothing is public. Next:" + chr(10) +
              "  python tools/zenodo_doi_writeback.py" + chr(10) +
              "  quarto render" + chr(10) +
              "  python tools/zenodo_upload.py" + ("" if not args.sandbox else " --sandbox"))
    elif not args.publish:
        print("Drafts are not public yet. Review them on Zenodo, then re-run "
              "with --publish.")


if __name__ == "__main__":
    main()
