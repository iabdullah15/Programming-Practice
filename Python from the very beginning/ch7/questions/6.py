'''
Write a dictionary comprehension to reverse a dictionary, 
that is to make the keys in the original values and the values in the original keys. 
Why might thenew dictionary have a different size from the original?
'''

def reverse_dict(d: dict):
    
    new_dict = {value:key for key, value in d.items()}
    
    return new_dict


d = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(reverse_dict(d))