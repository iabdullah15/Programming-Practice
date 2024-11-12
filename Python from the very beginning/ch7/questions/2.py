'''
2.
Write a function unzip which, given a dictionary, 
returns a pair of lists, the first containing the 
keys and the second the corresponding values.
'''

def unzip(d: dict):

    l1 = []
    l2 = []

    for key, value in d.items():
        
        l1.append(key)
        l2.append(value)

    return l1, l2

d = {1: 'one', 2: 'two', 3: 'three'}
l1, l2 = unzip(d)
print(f"List 1: {l1}")
print(f"List 2: {l2}")