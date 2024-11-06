'''
Write a function to print the minimum and maximum numbers in a list. You may assume the list is non-empty.
'''


def minimum(l: list):

    min_val = l[0]

    for x in l:

        if x < min_val:
            min_val = x

    return min_val


def maximum(l: list):

    max_val = l[0]

    for x in l:

        if x > max_val:

            max_val = x

    return max_val


l = [1, 2, 3, 4]
# l = [1, 2, 3, 4, 5, 5, 6, 7, 8, 89, 0]

print(f"Min in list is: {minimum(l)}")

print(f"Max in list is: {maximum(l)}")
