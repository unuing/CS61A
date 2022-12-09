def wears_jacket_with_if(temp, raining):
    """Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
    Write a function that takes in the current temperature and a boolean value telling
    if it is raining and returns True if Alfonso will wear a jacket and False otherwise.
    First, try solving this problem using an if statement.

    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False


def wears_jacket(temp, raining):
    """Note that we'll either return True or False based on a single condition, whose
    truthiness value will also be either True or False. Knowing this, try to write this
    function using a single line.

    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp < 60 or raining


def is_prime(n):
    """returns True if a positive integer n is a prime number and False otherwise.

    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True