#!/usr/bin/env python3
"""
Split a manuscript in `manuscripts/` into the `_NN-*.qmd` chapter fragments.

Prose goes through a pandoc markdown round-trip. That is what turns a bare URL
into an `<autolink>` and escapes `$` and `~`. Skipping it is not cosmetic: a
references chapter written with bare URLs renders as plain text, and Report 10
shipped that way until this tool was written.

Three things have to be right, each learned by reproducing an already-published
report byte for byte:

* **TeX math off.** The reports quote dollar amounts, and `$1 billion ...
  $9 billion` otherwise parses as a math span.
* **Read the result from a file, never from stdout.** `quarto pandoc` clips its
  stdout on Windows, dropping a ~2 KB chunk mid-word with no error and a zero
  exit code. The length guard below is the backstop.
* **Tables pass through verbatim.** pandoc would rewrite a compact pipe table
  as a multiline table; every committed fragment keeps the compact form.
  Column alignment (`|---:|`) is part of the table and survives with it.

`tbl-colwidths` exists only in the qmd, never in the manuscript, so it is
re-attached here per table — a fragment regenerated without it silently loses
the column proportions.

Usage:
    python tools/split_manuscript.py r08 --check
    python tools/split_manuscript.py r08 --write
"""
import argparse, io, os, re, subprocess, sys

READER = 'markdown-smart-tex_math_dollars+autolink_bare_uris'
WRITER = 'markdown-smart'
SCRATCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.split-tmp')


def roundtrip(text):
    if not text.strip():
        return text
    os.makedirs(SCRATCH, exist_ok=True)
    src, dst = os.path.join(SCRATCH, 'in.md'), os.path.join(SCRATCH, 'out.md')
    io.open(src, 'w', encoding='utf-8', newline='\n').write(text)
    p = subprocess.run(['quarto', 'pandoc', '-f', READER, '-t', WRITER,
                        '--wrap=none', src, '-o', dst],
                       capture_output=True, shell=(os.name == 'nt'))
    if p.returncode:
        sys.exit('pandoc failed: ' + p.stderr.decode('utf-8', 'replace')[:400])
    out = io.open(dst, encoding='utf-8').read().replace('\r\n', '\n')
    if len(out) < len(text) * 0.9:
        sys.exit('pandoc returned less than it was given (%d -> %d) — see the '
                 'stdout note above' % (len(text), len(out)))
    return out


def convert(chunk, widths=None):
    lines, out, buf, i, n = chunk.split('\n'), [], [], 0, 0

    def flush():
        if buf:
            out.append(roundtrip('\n'.join(buf).strip('\n') + '\n').strip('\n'))
            del buf[:]

    while i < len(lines):
        if lines[i].startswith('|'):
            j = i
            while j < len(lines) and lines[j].startswith('|'):
                j += 1
            flush()
            out.append('\n'.join(lines[i:j]))
            if widths:
                out.append(': {tbl-colwidths="%s"}' % widths[n])
            n += 1
            i = j
        else:
            buf.append(lines[i])
            i += 1
    flush()
    if widths is not None and n != len(widths):
        sys.exit('expected %d tables, found %d' % (len(widths), n))
    return '\n\n'.join(s for s in out if s.strip()) + '\n'


def split_chapters(text):
    """Chapters are the level-1 headings of the body, after the front matter."""
    body = text.split('\n---\n', 1)[1].split('\n---\n', 1)[1]
    lines = body.split('\n')
    heads = [i for i, l in enumerate(lines) if l.startswith('# ')] + [len(lines)]
    return [(lines[a][2:].strip(), '\n'.join(lines[a + 1:b]).strip('\n'))
            for a, b in zip(heads, heads[1:])]


def widths_of(path):
    """Read back the column widths a fragment already carries, so regenerating
    it keeps them."""
    if not os.path.exists(path):
        return None
    found = re.findall(r'^: \{tbl-colwidths="([^"]+)"\}$',
                       io.open(path, encoding='utf-8').read(), re.M)
    return found or None


def hand_built(path):
    """True if the fragment carries structure this tool cannot reproduce.

    A table whose PDF and web proportions differ is written twice, inside
    `.content-visible` blocks, and only in the qmd -- the manuscript keeps one
    copy. Regenerating from the manuscript would collapse it back to one table
    and silently drop the print widths, so refuse instead."""
    if not os.path.exists(path):
        return False
    return '.content-visible' in io.open(path, encoding='utf-8').read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('report', help='report directory name, e.g. r08')
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write', action='store_true', help='overwrite the fragments')
    g.add_argument('--check', action='store_true', help='report differences only')
    args = ap.parse_args()

    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    os.chdir(root)
    ms = [f for f in os.listdir('manuscripts') if f.startswith(args.report + '-')]
    if len(ms) != 1:
        sys.exit('expected one manuscript for %s, found %s' % (args.report, ms))
    text = io.open(os.path.join('manuscripts', ms[0]), encoding='utf-8').read()

    d = os.path.join('reports', args.report)
    names = sorted(f for f in os.listdir(d) if re.match(r'^_\d\d-.*\.qmd$', f))
    chunks = split_chapters(text)
    if len(chunks) != len(names):
        sys.exit('%d chapters but %d fragments — a split chapter needs the '
                 'boundary given by hand' % (len(chunks), len(names)))

    rc = 0
    for (title, chunk), name in zip(chunks, names):
        path = os.path.join(d, name)
        if hand_built(path):
            print('%-30s SKIPPED -- hand-built per-format tables' % name)
            rc |= 2
            continue
        new = convert(chunk, widths_of(path))
        old = io.open(path, encoding='utf-8').read().replace('\r\n', '\n') \
            if os.path.exists(path) else None
        if args.write:
            io.open(path, 'w', encoding='utf-8', newline='\n').write(new)
            print('%-30s %s' % (name, 'unchanged' if new == old else 'written'))
        else:
            same = new == old
            rc |= 0 if same else 1
            print('%-30s %s' % (name, 'matches' if same else 'DIFFERS'))
    return rc


if __name__ == '__main__':
    sys.exit(main())
