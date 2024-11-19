def remove_zeroes(x: list):

    l = [i for i in x if i != 0]

    return l


l = [1, 0, 1, 2, 3, 4, 5, 65, 234, 43, 1, 0, 0, 12, 0, 1, 34, 4, 45, 234, 0]
print(remove_zeroes(l))