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


def validate_poem(poem: str) -> None:
    length = len(poem)
    if not 1 <= length <= 280:
        raise ValueError(
            f"Poem must contain between 1 and 280 Unicode code points; got {length}."
        )


def main():
    validate_poem(POEM)
    poem_bytes = POEM.encode("utf-8")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_bytes(poem_bytes)
    os.chmod(output_path, 0o644)

    if output_path.read_bytes() != poem_bytes:
        raise RuntimeError(
            f"Verification failed: {output_path} does not match the intended poem."
        )


if __name__ == "__main__":
    main()
