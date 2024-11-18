'''
4. Write the function union(a, b) which forms the union of two dictionaries. 
The union of two dictionaries is the dictionary containing all the entries in one or other or both. 
In the case that a key is contained in both dictionaries, the value in the first should be preferred.
'''

def union(a: dict, b: dict):
    
    d = {}
    
    for key, value in a.items():
                    
        d[key] = value
    
    for key, value in b.items():
        
        if key not in d:
            
            d[key] = value
            
    
    return d
    
    
a = {1:'a', 2: 'b', 3:'c'}
b = {4:'a', 3: 'b', 6:'c'}
d = union(a, b)

print(d)