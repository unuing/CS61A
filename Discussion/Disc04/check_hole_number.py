def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    if n < 1000:
        return n // 100 > n // 10 % 10 and n % 10 > n // 10 % 10
    return check_hole_number(n % 1000) and check_hole_number(n // 100)