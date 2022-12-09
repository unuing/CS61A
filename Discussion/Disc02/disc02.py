def keep_ints(cond, n):
    for i in range(1, n + 1):
        if cond(i):
            print(i)


def make_keeper(n):
    def f(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)
    
    return f


def print_delayed(x):
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print


def print_n(n):
    def inner_print(arg):
        if n <= 0:
            print("done")
        else:
            print(arg)
        return print_n(n - 1)
    
    return inner_print