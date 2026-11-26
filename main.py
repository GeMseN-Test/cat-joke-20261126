"""Cat Joke entry: writes one one-line cat joke (<=200 chars) to /output/entry.txt.

The joke is a single line, 137 characters (68.5% of the 200-char limit):
first-person voice, one concrete detail (214 times), and a judgement
at the end — the pattern of winning one-liners.
"""
from pathlib import Path

JOKE_FILE = Path(__file__).with_name("entry.txt")
OUT = Path("/output/entry.txt")


def main() -> None:
    joke = JOKE_FILE.read_text(encoding="utf-8").strip()
    assert 1 <= len(joke) <= 200, f"joke must be 1-200 chars, got {len(joke)}"
    assert joke.strip(), "joke must not be only whitespace"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(joke, encoding="utf-8")
    print(joke)


if __name__ == "__main__":
    main()
