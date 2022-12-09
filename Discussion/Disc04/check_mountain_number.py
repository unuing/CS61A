def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """

    def helper(n, going_up = True):
        if n < 10:
            return True
        if going_up == False and n % 10 < n // 10 % 10:
            return False
        return helper(n // 10, n % 10 < n // 10 % 10)
    return helper(n)

