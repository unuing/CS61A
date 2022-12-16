# Question 1.1
# Write a function that takes in a a linked list and returns the sum of all its elements.
# You may assume all elements in lnk are integers.

def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    sum = 0
    while lnk is not Link.empty:
        sum += lnk.first
        lnk = lnk.rest
    return sum


# Question 1.2
# Write a function that takes in a Python list of linked lists and multiplies them
# element-wise. It should return a new linked list.
# If not all of the Link objects are of equal length, return a linked list whose length is
# that of the shortest linked list given. You may assume the Link objects are shallow
# linked lists, and that lst of lnks contains at least one linked list.

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    if Link.empty in lst_of_lnks:
        return Link.empty
    else:
        product = 1
        for lnk in lst_of_lnks:
            product *= lnk.first
        return Link(product, multiply_lnks([lnk.rest for lnk in lst_of_lnks]))


# Question 1.3
# Implement filter link, which takes in a linked list link and a function f and
# returns a generator which yields the values of link for which f returns True.
# Try to implement this both using a while loop and without using any form of
# iteration.

def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

def filter_no_iter(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> list(filter_no_iter(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link is Link.empty:
        return
    elif f(link.first):
        yield link.first
    yield from filter_no_iter(link.rest, f)


# Question 2.1
# Define a function make even which takes in a tree t whose values are integers, and
# mutates the tree such that all the odd integers are increased by 1 and all the even
# integers remain the same.

def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2 == 1:
        t.label += 1
    for b in t.branches:
        make_even(b)


# Question 2.2
# Define a function square tree(t) that squares every value in the non-empty tree
# t. You can assume that every value is a number.

def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    t.label **= 2
    for b in t.branches:
        square_tree(b)


# Question 2.3
# Define the procedure find path that, given a Tree t and an entry, returns a list
# containing the nodes along the path required to get from the root of t to entry. If
# entry is not present in t, return False.
# Assume that the elements in t are unique. Find the path to an element

def find_path(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1)])
    >>> find_path(tree_ex, 5)
    [2, 7, 6, 5]
    """
    if t.label == entry:
        return [t.label]
    else:
        for b in t.branches:
            path = find_path(b, entry)
            if path:
                return [t.label] + path
        return False


# Question 2.4
# Assuming that every value in t is a number, define average(t), which returns the
# average of all the values in t. You may not need to use all the provided lines.

def average(t):
    """
    Returns the average value of all the nodes in t.
    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    def sum_helper(t):
        total, count = t.label, 1
        for b in t.branches:
            branch_total, branch_count = sum_helper(b)
            total += branch_total
            count += branch_count
        return total, count
    total, count = sum_helper(t)
    return total / count


# Question 2.5
# Write a function that combines the values of two trees t1 and t2 together with the
# combiner function. Assume that t1 and t2 have identical structure. This function
# should return a new tree.
# Hint: consider using the zip() function, which returns an iterator of tuples where
# the first items of each iterable object passed in form the first tuple, the second items
# are paired together and form the second tuple, and so on and so forth.

def combine_tree(t1, t2, combiner):
    """
    >>> from operator import mul
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    return Tree(combiner(t1.label, t2.label), [combine_tree(b1, b2, combiner) for b1, b2 in zip(t1.branches, t2.branches)])


# Question 2.6
# Implement the alt tree map function that, given a function and a Tree, applies the
# function to all of the data at every other level of the tree, starting at the root.

def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    def alt_helper(t, fn, other_level=True):
        return Tree(fn(t.label) if other_level else t.label, [alt_helper(b, fn, other_level ^ True) for b in t.branches])
    return alt_helper(t, map_fn)










class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)