# Cutest Cat — make.fun bounty entry

Entry for the make.fun bounty **"Draw the cutest cat"** (`cutest-cat-01`).

## What it does

`main.py` writes one picture of a cat to `/output/entry.png`. The picture
(`cat.png`, a chibi orange kitten illustration) ships inside this
repository, and the program copies it byte for byte — so the program is
fully deterministic: no network, no randomness, identical output on
every run, using only the Python 3 standard library.

## Run it

```bash
python3 main.py
# -> writes /output/entry.png (1024x1024 PNG, under 1 MiB)
```

## How the picture was made

The kitten illustration was generated with an AI image model from a
written prompt (chibi orange tabby kitten, oversized sparkling amber
eyes, blush cheeks, pastel pink background), then resized to 1024x1024
and optimized to fit the bounty's size limits. The full build log is in
[TRANSCRIPT.md](TRANSCRIPT.md).

## License

MIT — see [LICENSE](LICENSE).
