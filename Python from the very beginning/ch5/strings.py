'''
Splitting and joining
We can split a string into a list of its letters, each as a string, using the built-in list function:
'''

myStr=list('tumultous')
print(myStr)

'''
We might think the reverse can be achieved using the familiar built-in
str function, but that just builds a string showing how the list would be printed by Python:
'''

print(str(myStr))

'''
We could write a function to do it ourselves:
'''

def join(l: list[str]):
    
    s = ''
    for char in l:
        s+=char
    return s

print(join(myStr))

'''
As you might suspect, there is a built-in join function:  it is, somewhatcounterintuitively, a method on strings. 
We specify the empty string and we see this:
'''
l = list('tumultuous')
print(''.join(l))


'''
Another method on strings is
split, which splits a given string into a list ofstrings, one for each word in the original:
'''
s = ' Once upon a time '
print(s.split())

'''
Finding strings in other strings
The find method gives the index of the first position a string appears in another:
'''

print(s.find('upon'))