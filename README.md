# BCtCI-DSA-Solutions

Python solutions to data structures & algorithms problems from **_Beyond Cracking the Coding Interview_** (BCtCI) by Gayle Laakmann McDowell, Mike Mroczka, Aline Lerner, and Nil Mamano.

This repo is my personal practice log as I work through the book — one problem at a time, with clean code, runnable test cases, and notes on the approach.

---

## About the book

_Beyond Cracking the Coding Interview_ (2025) is the follow-up to the classic _Cracking the Coding Interview_. It covers 24 core DSA topics for technical interviews, including two pointers, sliding windows, binary search, trees, graphs, heaps, backtracking, dynamic programming, topological sort, and more.

This repo tracks my solutions as I go through the book's problems.

---

## Repository structure

Problems are organized into folders by topic. Each file solves a single problem and is named after the problem and the page number in the book, so it's easy to cross-reference.

```
BCtCI-DSA-Solutions/
├── trees/
│   ├── warmup_problem_page_430.py
│   ├── warmup_problem_page_431.py
│   ├── DFS_page_435.py
│   ├── problem_page_436.py
│   ├── problem_Aligned_Chain_page_436.py
│   ├── problem_Hidden_Message_page_437.py
│   ├── problem_triangle_count_page_438.py
│   ├── problem_tree_layout_page_438.py
│   └── problem_invert_binary_tree_page_439.py
├── .gitignore
└── README.md
```

More topic folders will be added as I work through the book (arrays, strings, two pointers, binary search, graphs, heaps, DP, etc.).

### File naming convention

```
<problem_name>_page_<page_number>.py
```

- `problem_name` — short description of the problem in `snake_case`
- `page_number` — page in _Beyond Cracking the Coding Interview_ where the problem appears

Warm-up / easier exercises use the `warmup_` prefix.

---

## File layout

Each solution file typically contains:

1. The data structure definitions needed (e.g. `class Node` for tree problems)
2. The solution function(s) with a clear name
3. A `__main__` block with test cases that print `OK` / `FAIL` / `ERROR` and a summary

Example structure:

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root):
    # solution here
    ...


if __name__ == "__main__":
    cases = [
        ("test name", input, expected_output),
        # ...
    ]

    passed = failed = errors = 0
    for name, inp, expected in cases:
        try:
            got = solve(inp)
            if got == expected:
                print(f"{name}: got={got}, expected={expected} -> OK")
                passed += 1
            else:
                print(f"{name}: got={got}, expected={expected} -> FAIL")
                failed += 1
        except Exception as e:
            print(f"{name}: ERROR ({type(e).__name__}: {e})")
            errors += 1

    print(f"--- summary: OK={passed}, FAIL={failed}, ERROR={errors}")
```

---

## Running a solution

Every file is self-contained and runnable.

Requirements:

- Python 3.9+ (any recent Python 3 should work — no external dependencies)

Run any problem directly:

```bash
python trees/problem_tree_layout_page_438.py
```

You'll see each test case's result and a summary line at the end.

Run all problems in a folder:

```bash
for f in trees/*.py; do
  echo "=== $f ==="
  python "$f"
done
```

---

## Progress

| Topic | Folder | Problems solved |
| ----- | ------ | --------------- |
| Trees | [`trees/`](./trees) | 9 |

More topics coming as I progress through the book.

---

## Notes

- These solutions are **my own work**. Problem statements are referenced by page number only — no text is copied from the book, out of respect for the authors' copyright. If you want the actual problem descriptions, please buy the book at [bctci.co](https://www.bctci.co/).
- Solutions aim to be correct and readable first, then efficient. Where relevant, I'll add comments on time/space complexity and alternative approaches.
- If you spot a bug, a cleaner solution, or a missing edge case, feel free to open an issue or PR.

---

## License

Code in this repository is released under the [MIT License](./LICENSE). The book itself and its problem statements are the property of their respective authors and publisher.

---

## Disclaimer

This is an unofficial, independent study repository. It is not affiliated with or endorsed by the authors or publisher of _Beyond Cracking the Coding Interview_.

## Author 👤

**Shivay Bajaj**

- GitHub: https://github.com/IDropCoins
