def count_stair_ways(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)