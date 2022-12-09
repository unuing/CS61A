def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 0:
        return 0
    if n == 1:
        return m
    half = n // 2
    return multiply(m, half) + multiply(m, n - half)