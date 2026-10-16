"""Readable examples of several ways to reverse text in Python."""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence


def reverse_for_loop(text: str) -> str:
    """Return text reversed by prepending characters in a for loop."""
    result = ""
    for character in text:
        result = character + result
    return result


def reverse_while_loop(text: str) -> str:
    """Return text reversed by walking its indexes from right to left."""
    result = ""
    index = len(text) - 1
    while index >= 0:
        result += text[index]
        index -= 1
    return result


def reverse_slice(text: str) -> str:
    """Return text reversed with Python's extended-slice syntax."""
    return text[::-1]


def reverse_builtin(text: str) -> str:
    """Return text reversed with reversed() and str.join()."""
    return "".join(reversed(text))


def reverse_recursive(text: str) -> str:
    """Return text recursively (educational; unsuitable for long input)."""
    if len(text) <= 1:
        return text
    return reverse_recursive(text[1:]) + text[0]


METHODS: dict[str, Callable[[str], str]] = {
    "for": reverse_for_loop,
    "while": reverse_while_loop,
    "slice": reverse_slice,
    "builtin": reverse_builtin,
    "recursive": reverse_recursive,
}


def reverse_words(text: str) -> str:
    """Reverse word order while normalizing runs of whitespace."""
    return " ".join(text.split()[::-1])


def reverse_each_word(text: str) -> str:
    """Reverse every word while preserving spaces between words."""
    return " ".join(reverse_slice(part) for part in text.split(" "))


def is_palindrome(text: str, *, ignore_case: bool = True) -> bool:
    """Check if text is a palindrome, ignoring punctuation and spaces."""
    normalized = "".join(character for character in text if character.isalnum())
    if ignore_case:
        normalized = normalized.casefold()
    return normalized == reverse_slice(normalized)


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Reverse text using one of five Python techniques."
    )
    parser.add_argument("text", nargs="?", help="text to reverse")
    parser.add_argument(
        "-m", "--method", choices=METHODS, default="slice",
        help="reversal technique (default: slice)",
    )
    parser.add_argument("--words", action="store_true", help="reverse word order")
    parser.add_argument("--each-word", action="store_true", help="reverse each word")
    parser.add_argument("--palindrome", action="store_true", help="check for a palindrome")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line interface and return a process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)
    text = args.text if args.text is not None else input("Enter text: ")
    if sum((args.words, args.each_word, args.palindrome)) > 1:
        parser.error("choose only one of --words, --each-word, or --palindrome")
    if args.palindrome:
        print("Yes" if is_palindrome(text) else "No")
    elif args.words:
        print(reverse_words(text))
    elif args.each_word:
        print(reverse_each_word(text))
    else:
        print(METHODS[args.method](text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
