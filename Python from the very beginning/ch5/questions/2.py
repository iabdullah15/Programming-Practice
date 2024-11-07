'''
2. Use sorted to write a similar function to q1.
'''

def sort_words(s: str):
    
    l = s.split()
    l = sorted(l)
    
    return ' '.join(l)

s = 'this is a sentence which will get sorted by my function'
print(sort_words(s))