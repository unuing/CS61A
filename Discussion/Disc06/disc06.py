# Question 1.2
# Write a function that takes in a number n and returns a one-argument function.
# The returned function takes in a function that is used to update n. It should return
# the updated n.

def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def update(f):
        nonlocal n
        n = f(n)
        return n
    return update


# Question 2.2
# Write a function that takes in no arguments and returns two functions, prepend and
# get, which represent the “add to front of list” and “get the ith item” operations,
# respectively. Do not use any python built-in data structures like lists or dictionaries.
# You do not necessarily need to use all the lines.

def nonlocalist():
    """
    >>> prepend, get = nonlocalist()
    >>> prepend(2)
    >>> prepend(3)
    >>> prepend(4)
    >>> get(0)
    4
    >>> get(1)
    3
    >>> get(2)
    2
    >>> prepend(8)
    >>> get(2)
    3
    """
    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = get
        def get(i):
            if i == 0:
                return value
            return f(i - 1)
    return prepend, lambda x: get(x)   # using only `get` here will return the lambda function indicating index out of range


# Question 2.3
# Fill in the definition of f below such that the interpreter prints as expected. Your
# solution must be on one line.
"""
>>> f = lambda x: x and (f(x - 1) or print(x))
>>> f = f(10)
1
2
3
4
5
6
7
8
9
10
"""
# Then, given your definition of f, what will be printed below? (Assuming that the
# above lines have also been executed in the interpreter.)
"""
>>> f
None
"""


# Question 2.5
# It’s Hog again! Write a commentary function announce losses that takes in a player
# who and returns a commentary function that announces whenever that player loses
# points.

def announce_losses(who, last_score=0):
    """
    >>> f = announce_losses(0)
    >>> f1 = f(10, 0)
    >>> f2 = f1(1, 10) # Player 0 loses points due to swine swap
    Oh no! Player 0 just lost 9 point(s).
    >>> f3 = f2(7, 10)
    >>> f4 = f3(7, 11) # Should not announce when player 0's score does not change
    >>> f5 = f4(11, 12)
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    def say(score0, score1):
        if who == 0:
            score = score0
        elif who == 1:
            score = score1
        if score < last_score:
            print("Oh no! Player {0} just lost {1} point(s).".format(who, last_score - score))
        return announce_losses(who, score)
    return say


# Question 2.6
# (Fall 2013) The CS 61A staff has developed a formula for determining what a fox
# might say. Given three strings—a start, a middle, and an end—a fox will say the
# start string, followed by the middle string repeated a number of times, followed by
# the end string. These parts are all separated by single hyphens.
# Complete the definition of fox says, which takes the three string parts of the fox’s
# statement (start, middle, and end) and a positive integer num indicating how many
# times to repeat middle. It returns a string. You cannot use any for or while
# statements. Use recursion in repeat. Moreover, you cannot use string operations
# other than the + operator to concatenate strings together

def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(k):
        if k == 1:
            return middle
        return middle + '-' + repeat(k - 1)
    return start + '-' + repeat(num) + '-' + end


# Question 2.7

def primary_stress(t):
    """
    >>> word = tree("", [ \
        tree("w", [tree("s", [tree("min")]), tree("w", [tree("ne")])]), \
        tree("s", [tree("s", [tree("so")]), tree("w", [tree("ta")])])])
    >>> primary_stress(word)
    'so'
    >>> phrase = tree("", [ \
        tree("s", [tree("s", [tree("law")]), tree("w", [tree("degree")])]), \
        tree("w", [tree("requirement")])])
    >>> primary_stress(phrase)
    'law'
    """
    def helper(t, num_s):
        if is_leaf(t):
            return [label(t), num_s]
        if label(t) == "s":
            num_s = num_s + 1
        return max([helper(b, num_s) for b in branches(t)],
            key = lambda x: x[1])
    return helper(t, 0)[0]


# Question 2.8
# Consider the subset sum problem: you are given a list of integers and a number k.
# Is there a subset of the list that adds up to k?

def subset_sum(seq, k):
    """
    >>> subset_sum([2, 4, 7, 3], 5) # 2 + 3 = 5
    True
    >>> subset_sum([1, 9, 5, 7, 3], 2)
    False
    >>> subset_sum([1, 1, 5, -1], 3)
    False
    """
    if seq == []:
        return False
    if k in seq:
        return True
    return subset_sum(seq[1:], k - seq[0]) or subset_sum(seq[1:], k)




# Tree ADT

# Constructor
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selector
def label(tree):
    """Return the label value of a tree."""
    return tree[0]

# Selector
def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

# For convenience
def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise."""
    return not branches(tree)
