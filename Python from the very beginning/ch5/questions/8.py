'''
Rewrite your clip_list example from question 6 in the form of a list comprehension.
'''

def clip(val: int):
    
    if val < 1:
        return 1
    elif val > 10:
        return 10
    else:
        return val
    
l = [clip(i) for i in range(-4, 20, 2)]
print(l)