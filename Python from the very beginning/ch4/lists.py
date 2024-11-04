l = ['zero', 'one', 'two', 'three', 'four', 'five']
l2 = [2, 3, 5, 7, 11, 13]

print(f"Len of list1 {len(l)} Len of list2 {len(l2)}")

# Iterating:

for x in l2:
    print(x, end=" ")
    
print()

'''
Sometimes we need both the index in the list and the item at that index. By using
enumerate, and giving two names - one for the index and one for the value - we can do this easily:
'''

for i, el in enumerate(l):
    
    print(f"{i}: {el}")
    
'''
List slices
We can pick parts of the list out using what is called a
slice. A slice is defined using start and stop positions:
'''

print(l[0:3])

'''
Notice that the stop value defines the position to stop before, just like with a
range. We may omit the start or stop value. This will then be taken to stretch to the omitted end of the list:
'''

print(l[2:])

if 'two' in l:
    print("TWO IN L")

if 'six' not in l:
    print("SIX NOT IN L")

print(l.index("two"))
print(l.count('two'))

l3 = list(range(1,11))
print(l3)