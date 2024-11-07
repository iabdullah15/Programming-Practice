'''
4.
Write a function to remove spaces from the beginning and end of a string 
representing a sentence by converting the string to a list of its letters, processing it, 
and converting it back to a single string. 
You might find thebuilt-in reverse method on lists useful, or another list-reversal mechanism.
'''

def remove_spaces(s: str):
    
    l = s.split()
    return ' '.join(l)    

s = '           this is a sentence which will get sorted by my function                      '
print(remove_spaces(s))