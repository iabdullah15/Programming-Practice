'''
1. Use the sort method to build a function which returns an alphabetically 
sorted list of all the words in a given sentence.
'''


def sort_words(s: str):

    l = s.split()
    print(l)
    l.sort()
    s = ' '.join(l)

    return s


s = 'this is a sentence which will get sorted by my function'
print(sort_words(s))
