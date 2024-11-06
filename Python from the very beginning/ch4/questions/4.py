'''
4.
As well as start and stop positions, a slice may have a third part, the step (just like a step in a range ). For example l[0:10:2] . 
Write a function evens to return a list containing the items at even positions 0, 2, … in the given list.
'''

def evens(l: list):
    
    even_els = l[0: len(l): 2]
    
    return even_els

l = [1, 2, 3, 4, 5, 5, 6, 7, 8, 89, 0]

for i, val in enumerate(l):
    print(f"i {i}: {val}")

print(evens(l))