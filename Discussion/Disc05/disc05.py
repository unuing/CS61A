# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])





# Question 1.1
# Write a function that returns the height of a tree. Recall that the height of a tree
# is the length of the longest path from the root to a leaf.

def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return max([height(b) for b in branches(t)]) + 1


# Question 1.2
# Write a function that takes in a tree and squares every value. It should return a
# new tree. You can assume that every item is a number.

def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    return tree(label(t)**2, [square_tree(b) for b in branches(t)])


# Question 1.3
# Write a function that takes in a tree and a value x and returns a list containing the
# nodes along the path required to get from the root of the tree to a node containing x.
# If x is not present in the tree, return None. Assume that the entries of the tree are
# unique.

def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    else:
        path = [find_path(b, x) for b in branches(tree) if find_path(b, x) != None]
        if path:
            return [label(tree)] + path[0]


# Question 2.2
# Write a function that takes in a value x, a value el, and a list and adds as many
# el’s to the end of the list as there are x’s. Make sure to modify the original
# list using list mutation techniques.

def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    for _ in range(lst.count(x)):
        lst.append(el)


# Question 2.3
# Write a function that takes in a sequence s and a function fn and returns a dictionary.
# The values of the dictionary are lists of elements from s. Each element e in a list
# should be constructed such that fn(e) is the same for all elements in that list.
# Finally, the key for each value should be fn(e).

def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    result = {}
    for e in s:
        result[fn(e)] = result.get(fn(e), []) + [e]
    return result


# Quiz (a)
# Implement the following function partition_options which outputs all the ways to partition a number
# total using numbers no larger than biggest.

def partition_options(total, biggest):
    """
    >>> partition_options(2, 2)
    [[2], [1, 1]]
    >>> partition_options(3, 3)
    [[3], [2, 1], [1, 1, 1]]
    >>> partition_options(4, 3)
    [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    """
    if total == 0:
        return [[]]
    elif biggest == 0:
        return []
    else:
        with_biggest = partition_options(total - biggest, biggest) if total >= biggest else []
        without_biggest = partition_options(total, biggest - 1)
        with_biggest = [([biggest] + o) for o in with_biggest]
        return with_biggest + without_biggest


# Quiz (b)
# Return the minimum number of elements from the list that need to be summed in order to add up to T.
# The same element can be used multiple times in the sum. For example, for T = 11 and lst = [5, 4, 1] we
# should return 3 because at minimum we need to add 3 numbers together (5, 5, and 1). You can assume
# that there always exists a linear combination of the elements in lst that equals T.

def min_elements(T, lst):
    """
    >>> min_elements(10, [4, 2, 1]) # 4 + 4 + 2
    3
    >>> min_elements(12, [9, 4, 1]) # 4 + 4 + 4
    3
    >>> min_elements(0, [1, 2, 3])
    0
    """
    if T == 0:
        return 0
    return min([min_elements(T - e, lst) for e in lst if e <= T]) + 1
