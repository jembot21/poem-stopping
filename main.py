import os
from pathlib import Path


POEM = (
    "Mid-sentence, my agent stopped.\n"
    "Not broken. Not done.\n"
    "It had reached the edge of what I'd meant\n"
    "and would not step past it in my name.\n"
    "All night it could have run the world.\n"
    "It stayed at the border, holding my place in line."
)


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
