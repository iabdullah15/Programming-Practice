def copy_list(l: list):
    
    new_l = []
    
    for x in l:
        new_l.append(x)
        
    return new_l

def remove_el(l: list, element):
    
    new_l = copy_list(l)
    
    for i in range(len(new_l)):
        
        if element == new_l[i]:
            
            new_l.pop(i)
            return new_l
        
    return "Element does not exist"
    
my_l = [1,2,3,4,5,6]

l = remove_el(my_l, 5)
print(f"After removing: {l}")