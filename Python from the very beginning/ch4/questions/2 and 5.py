# Write a function to build a new list which is the reverse of a given list.

# def reverse_list(l: list):
    
#     reversed_list = []
        
#     for i in range((len(l)-1), -1, -1):
        
#         reversed_list.append(l[i])

#     return reversed_list       

#  
'''
5. A negative step value in a slice selects the elements from end to beginning.Use this to make your
reverse
function simpler.
'''


def reverse_list(l: list):
    
    return l[::-1]


l = [1,2,3,4]
l2 = reverse_list(l)
print(f"Reversed list is {l2}")