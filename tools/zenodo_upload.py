#!/usr/bin/env python3
"""
Create Zenodo records for every document in the manifest.

    python tools/zenodo_manifest.py > zenodo.json
    export ZENODO_TOKEN=...        # never committed, never passed on the CLI
    python tools/zenodo_upload.py --sandbox        # rehearse
    python tools/zenodo_upload.py                  # create real drafts
    python tools/zenodo_upload.py --publish        # mint the DOIs

Drafts by default. Publishing is the irreversible step -- a published Zenodo
record cannot be deleted, only a new version added -- so it needs the explicit
flag, and the script asks before doing it.

Progress is kept in a state file (`zenodo-state.json`, or
`zenodo-state-sandbox.json`), keyed by the document's URL, so a re-run resumes
rather than duplicating. Delete the state file only if you have also deleted
the drafts it names.

The token is read from the environment and is never written to the state file
or printed.
"""
import argparse, io, json, os, sys, time
import requests

TIMEOUT = 120


def api(base, token, method, path, **kw):
    url = path if path.startswith("http") else base + path
    for attempt in range(4):
        r = requests.request(method, url, timeout=TIMEOUT,
                             headers={"Authorization": "Bearer " + token}, **kw)
        if r.status_code not in (429, 500, 502, 503, 504):
            break
        wait = 2 ** attempt
        print("    %s %s -- retrying in %ds" % (r.status_code, r.reason, wait))
        time.sleep(wait)
    if not r.ok:
        sys.exit("%s %s failed: %s %s\n%s" % (method, url, r.status_code,
                                              r.reason, r.text[:600]))
    return r.json() if r.content else {}


def load(path):
    return json.load(io.open(path, encoding="utf-8")) if os.path.exists(path) else {}


def save(path, state):
    io.open(path, "w", encoding="utf-8", newline="\n").write(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--manifest", default="zenodo.json")
    p.add_argument("--sandbox", action="store_true",
                   help="use sandbox.zenodo.org; separate account and token")
    p.add_argument("--publish", action="store_true",
                   help="publish the drafts; this mints DOIs and cannot be undone")
    p.add_argument("--only", type=int, action="append",
                   help="restrict to these series positions (0 = Prologue, 15 = Epilogue)")
    args = p.parse_args()

    token = os.environ.get("ZENODO_TOKEN")
    if not token:
        sys.exit("set ZENODO_TOKEN (Zenodo > Applications > Personal access "
                 "tokens, scopes deposit:write and deposit:actions)")

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

        if not os.path.exists(rec["pdf"]):
            sys.exit("%s\n    missing %s -- run `quarto render` first"
                     % (label, rec["pdf"]))

        if not here.get("id"):
            dep = api(base, token, "POST", "/deposit/depositions",
                      json={}, headers={"Content-Type": "application/json"})
            here["id"] = dep["id"]
            here["bucket"] = dep["links"]["bucket"]
            here["draft"] = dep["links"].get("html")
            save(state_path, state)
            print("%s  draft %s" % (label, here["id"]))

        if not here.get("file"):
            name = os.path.basename(rec["pdf"])
            with io.open(rec["pdf"], "rb") as fh:
                api(base, token, "PUT", "%s/%s" % (here["bucket"], name), data=fh)
            here["file"] = name
            save(state_path, state)
            print("       uploaded %s" % name)

        api(base, token, "PUT", "/deposit/depositions/%s" % here["id"],
            json={"metadata": meta}, headers={"Content-Type": "application/json"})
        here["metadata_set"] = True
        save(state_path, state)

        if args.publish:
            out = api(base, token, "POST",
                      "/deposit/depositions/%s/actions/publish" % here["id"])
            here["doi"] = out.get("doi") or out.get("metadata", {}).get("doi")
            here["record"] = out["links"].get("record_html")
            save(state_path, state)
            print("       published %s" % here["doi"])

    done = sum(1 for v in state.values() if v.get("doi"))
    print("\n%d of %d published. State in %s."
          % (done, len(records), state_path))
    if not args.publish:
        print("Drafts are not public yet. Review them on Zenodo, then re-run "
              "with --publish.")


if __name__ == "__main__":
    main()
