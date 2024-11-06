''' 
1.
Write a function first to return the first element of a list, and a function
last to return the last element of the list. You may assume the list is non-empty.
'''

def first(l: list):

    return l[0]


def last(l: list):

    return l[-1]


l = [1, 2, 3, 4, 5, 5, 6, 7, 8, 89, 0]

print(f"First el: {first(l)}")
print(f"Last el: {last(l)}")