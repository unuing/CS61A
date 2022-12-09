def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """

    def prime_helper(number_to_devide):
        if number_to_devide == n:
            return True
        elif n % number_to_devide == 0:
            return False
        else:
            return prime_helper(number_to_devide + 1)

    return False if n == 1 else prime_helper(2)