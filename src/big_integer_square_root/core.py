def isqrt(n: int) -> int:
    """Floor of the square root of a non-negative integer ``n``.

    Returns the unique integer ``r`` with ``r*r <= n < (r+1)*(r+1)``.

    Uses Newton's method with exact integer division. We start from an
    over-estimate of the true root rather than from ``n`` itself: iterating
    ``x <- (x + n//x) // 2`` from any initial guess that is at least the
    true root is a monotone non-increasing descent that cannot overshoot
    below the root. A power-of-two bound is a cheap, exact over-estimate
    for arbitrary-size integers and keeps the whole computation in exact
    integer arithmetic (Python's ``int`` division truncates toward zero,
    which is what makes the floor behaviour fall out naturally).

    We special-case ``n < 2`` because the loop below would return ``1``
    for ``n == 1`` and we want the literal answer ``1``; ``0`` is handled
    for free by the same branch.

    The termination condition ``x > y`` is the standard two-variable form
    of Newton iteration: when the new iterate stops decreasing the current
    value is the floor of the root.
    """
    if n < 0:
        raise ValueError("isqrt argument must be non-negative")
    if n < 2:
        return n
    # Initial over-estimate: smallest power of two whose square exceeds n.
    # For n >= 2 this is at least the true root, which guarantees monotone
    # descent. Using 1 << ((n.bit_length() + 1) >> 1) would also work but
    # the extra +1 keeps the bound strictly above the root even for exact
    # powers, simplifying the termination argument.
    x = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        y = (x + n // x) >> 1
        if y >= x:
            return x
        x = y
