# (Spring 2015) Implement the memory function, which takes a number x and a single-
# argument function f. It returns a function with a peculiar behavior that you must
# discover from the doctests. You may only use names and call expressions in your
# solution. You may not write numbers or use features of Python not yet covered in
# the course.

square = lambda x: x * x
double = lambda x: 2 * x
def memory(x, f):
    """Return a higher-order function that prints its
    memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """
    def g(h):
        print(f(x))
        return memory(x, h)
    return g
