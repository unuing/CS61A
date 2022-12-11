# Question 2.1
# Write a generator function generate_subsets that returns all subsets of the positive
# integers from 1 to n. Each call to this generator’s next method will return a list of
# subsets of the set [1, 2, ..., n], where n is the number of previous calls to next.

def generate_subsets():
    """
    # >>> subsets = generate_subsets()
    # >>> for _ in range(3):
    # ...     print(next(subsets))
    # ...
    # [[]]
    # [[], [1]]
    # [[], [1], [2], [1, 2]]
    """
    def subsets(ls):
        if ls == []:
            return [[]]
        else:
            a = subsets(ls[1:])
            return a + [[ls[0]]+s for s in a]

    n = 0
    while True:
        yield subsets(list(range(1, n + 1)))
        n += 1
    

# Question 2.2
# Implement sum paths gen, which takes in a tree t and and returns a generator which
# yields the sum of all the nodes from a path from the root of a tree to a leaf.
# You may yield the sums in any order.

def sum_paths_gen(t):
    """
    >>> t1 = tree(5)
    >>> next(sum_paths_gen(t1))
    5
    >>> t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
    >>> sorted(sum_paths_gen(t2))
    [6, 7, 10]
    """
    if is_leaf(t):
        yield label(t)
    for b in branches(t):
        for s in sum_paths_gen(b):
            yield label(t) + s







# Tree ADT
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)