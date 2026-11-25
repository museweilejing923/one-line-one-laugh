"""One-line laugh writer.

Writes one fixed joke about password policy to /output/entry.txt.
Deterministic: no input, no network, no clock, no randomness.
"""

import os
import string
import sys

JOKE = "My password expired, so I changed it to the same password with a capital letter, and security has never felt stronger."
CAP = 140


def reject(why):
    print("error: " + why, file=sys.stderr)
    raise SystemExit(1)


def has_glued_sentences(line):
    """True when a sentence ends and the next starts with no space.

    A full stop, exclamation or question mark glued straight onto
    the next word (".So") is a typo, not a punchline. Only a capital
    letter counts as the next sentence starting, so "a.m." is fine.
    """
    for first, second in zip(line, line[1:]):
        if first in ".!?" and second.isupper():
            return True
    return False


def passes(line):
    if not line.strip():
        return "blank joke"
    if len(line) > CAP:
        return "over the 140-character limit"
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        return "control character inside"
    if line.strip() != line or "  " in line or "\n" in line:
        return "ragged spacing or a line break"
    if line[-1] not in ".!?":
        return "missing closing punctuation"
    if all(ch in string.punctuation for ch in line):
        return "punctuation only"
    if line.isdigit():
        return "digits only"
    if not any(ch.isalpha() for ch in line):
        return "no letters"
    if "password" not in line.lower():
        return "never mentions the password"
    if has_glued_sentences(line):
        return "two sentences glued together with no space"
    return ""


def main():
    problem = passes(JOKE)
    if problem:
        reject(problem)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(JOKE + "\n")


if __name__ == "__main__":
    main()
