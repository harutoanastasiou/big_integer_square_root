# Big Integer Square Root

Computes the integer floor of the square root of an arbitrarily large non-negative integer, using Newton's method with exact integer division.

```python
from big_integer_square_root import isqrt

assert isqrt(0) == 0
assert isqrt(8) == 2
assert isqrt(10**100 + 5) == 10**50
```

The single exported name is `isqrt(n: int) -> int`. It raises `ValueError` for negative input and otherwise returns the unique integer `r` with `r*r <= n < (r+1)*(r+1)`.

## Why this exists

Python's standard library gained `math.isqrt` in 3.8, so on modern CPython this package is redundant. It exists for environments where a pure-Python, dependency-free floor-square-root is wanted (older interpreters, alternative Python implementations without `math.isqrt`, or as a readable reference implementation).

The trade-off is speed: a pure-Python Newton iteration is dramatically slower than the C-backed `math.isqrt` for very large inputs, but it is portable and its correctness is easy to inspect.

## The awkward edge

There is no support for negative numbers or for returning the fractional part. Negative input raises `ValueError`; callers who want the complex square root should look elsewhere. The function is exact (no floating point is used at any point), so there is no rounding surprise at large magnitudes — only the integer floor.

## Tests

```
PYTHONPATH=src python -m unittest discover -s tests
```
