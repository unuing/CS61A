# Question 2.1
# Write a “macro” in Python called make lambda that takes in two parameters: params,
# a string containing a comma-separated list of variable names; and body, a Python
# expression in string form, and returns a lambda function that takes params as its
# parameters and body as its body.
def make_lambda(params, body):
    """
    >>> f = make_lambda("x, y", "x + y")
    >>> f
    <function <lambda> at ...>
    >>> f(1, 2)
    3
    >>> g = make_lambda("a, b, c", "c if a > b else -c")
    >>> g(1, 2, 3)
    -3
    >>> make_lambda("f, x, y", "f(x, y)")(f, 1, 2)
    3
    """
    return eval(f"lambda {params}: {body}")