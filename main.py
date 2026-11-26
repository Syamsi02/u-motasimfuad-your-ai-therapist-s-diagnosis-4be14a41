"""Write the AI therapist's diagnosis to /output/entry.txt.

Pure standard library, deterministic: the same single line every run.
"""

import os

DIAGNOSIS = (
    "Diagnosis: severe overthinking, terminal stage \u2014 you rehearsed "
    "this session in the shower, in traffic, and once more while reading "
    "this sentence."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = DIAGNOSIS.strip()
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space, on a single line.
    if not 1 <= len(text) <= 200:
        raise ValueError("diagnosis must be 1-200 characters")
    if text != text.strip() or "\n" in text:
        raise ValueError("diagnosis must be one clean line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
