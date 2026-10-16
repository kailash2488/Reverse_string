"""Tests for the reverse module."""

import subprocess
import sys
import unittest
from pathlib import Path

from reverse import METHODS, is_palindrome, reverse_each_word, reverse_words


ROOT = Path(__file__).resolve().parents[1]


class ReverseMethodsTests(unittest.TestCase):
    def test_every_method_reverses_text(self) -> None:
        for name, reverse in METHODS.items():
            with self.subTest(method=name):
                self.assertEqual(reverse("Hello, Python!"), "!nohtyP ,olleH")

    def test_every_method_handles_empty_text(self) -> None:
        for name, reverse in METHODS.items():
            with self.subTest(method=name):
                self.assertEqual(reverse(""), "")

    def test_every_method_handles_unicode(self) -> None:
        for name, reverse in METHODS.items():
            with self.subTest(method=name):
                self.assertEqual(reverse("नमस्ते"), "ेत्समन")


class UtilityTests(unittest.TestCase):
    def test_reverse_words(self) -> None:
        self.assertEqual(reverse_words("  learn   Python today "), "today Python learn")

    def test_reverse_each_word_preserves_spaces(self) -> None:
        self.assertEqual(reverse_each_word("hello  world"), "olleh  dlrow")

    def test_palindrome_ignores_case_and_punctuation(self) -> None:
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))

    def test_non_palindrome(self) -> None:
        self.assertFalse(is_palindrome("Python"))


class CommandLineTests(unittest.TestCase):
    def run_cli(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(ROOT / "reverse.py"), *arguments],
            check=False, capture_output=True, text=True,
        )

    def test_method_option(self) -> None:
        result = self.run_cli("abc", "--method", "builtin")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "cba")

    def test_palindrome_option(self) -> None:
        self.assertEqual(self.run_cli("racecar", "--palindrome").stdout.strip(), "Yes")


if __name__ == "__main__":
    unittest.main()
