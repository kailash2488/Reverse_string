# Reverse String in Python

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://github.com/kailash2488/Reverse_string/actions/workflows/tests.yml/badge.svg)](https://github.com/kailash2488/Reverse_string/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A beginner-friendly collection of **five ways to reverse a string in Python**, packaged as a reusable module and command-line tool. The examples use clear names, type hints, docstrings, and tests so learners can compare each technique with confidence.

## Quick start

No third-party packages are required:

```bash
python reverse.py "Hello, world!"
# !dlrow ,olleH
```

Choose any implementation:

```bash
python reverse.py "Python" --method for
python reverse.py "Python" --method while
python reverse.py "Python" --method slice
python reverse.py "Python" --method builtin
python reverse.py "Python" --method recursive
```

Run `python reverse.py --help` for every option. With no text argument, the program prompts for input.

## The five approaches

| Method | Idea | Time | Extra space | Best use |
|---|---|---:|---:|---|
| `for` | Prepend each character | O(n²) | O(n) | Learning loops |
| `while` | Read indexes right-to-left | O(n²) | O(n) | Learning indexes |
| `slice` | Use `text[::-1]` | O(n) | O(n) | Most Python code |
| `builtin` | Join `reversed(text)` | O(n) | O(n) | Working with iterators |
| `recursive` | Reverse tail, append head | O(n²) | O(n²) | Learning recursion only |

For production code, the slice version is generally the clearest. The recursive version can reach Python's recursion limit on long input.

## More useful examples

```bash
python reverse.py "learn Python today" --words
# today Python learn

python reverse.py "hello world" --each-word
# olleh dlrow

python reverse.py "A man, a plan, a canal: Panama!" --palindrome
# Yes
```

Use it as a module too:

```python
from reverse import is_palindrome, reverse_slice, reverse_words

print(reverse_slice("Hello"))                 # olleH
print(reverse_words("one two three"))         # three two one
print(is_palindrome("Never odd or even"))     # True
```

## Run the tests

```bash
python -m unittest discover -s tests -v
```

The suite covers empty input, whitespace, Unicode text, every method, utilities, and the CLI. GitHub Actions runs it on multiple Python versions.

> **Unicode note:** these examples reverse Unicode code points. Some visible symbols, such as emoji sequences or a letter plus a combining accent, contain multiple code points. Reversing user-perceived characters (grapheme clusters) requires a Unicode segmentation library.

## Contributing

Improvements are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Please add tests for behavior changes and keep examples approachable for beginners.

## License

Released under the [MIT License](LICENSE).
