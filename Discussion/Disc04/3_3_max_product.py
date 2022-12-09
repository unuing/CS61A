def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """

    if len(s) == 0:
        return 1
    if len(s) == 1:
        return s[0]
    
    use_first = s[0] * max_product(s[2:])
    dont_use_first = max_product(s[1:])
    return max(use_first, dont_use_first)