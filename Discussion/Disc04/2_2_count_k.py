def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """

    if n == 0 or n == 1:
        return 1
    result = 0
    for i in range(1, k + 1):
        start = n - i
        if start < 0:
            break
        result += count_k(start, k)
    return result
