'''
Write a function copy_list to copy a list in the 
same way as the copy method, but without using it.
'''

def copy_list(l: list):
    
    new_l = []
    
    for x in l:
        new_l.append(x)
        
    return new_l

l = [1,2,3,4]
new_l = copy_list(l)
print(l)
print(new_l)