'''
Write a function to detect if a given string is palindromic (i.e. equals its ownreverse).
Now use filter to write a function which takes a list of strings and returns only those which are palindromic. 
Then write a function to return a list of the numbers in a given range which are palindromic, 
for example 1331.
'''

def isPalindrome(s: str):
    
    s2 = ''.join(list(reversed(s)))
    return s == s2

def listIsPalindrome(l: list[str]):
    
    m = filter(isPalindrome, l)
    return list(m)


# List of palindrome strings
palindromes = ["racecar", "level", "madam", "rotor", "civic", "radar", "deified", "noon", "refer", "wow"]

# List of non-palindrome strings
non_palindromes = ["apple", "banana", "computer", "house", "table", "garden", "mountain", "school", "flower", "window"]

l = palindromes + non_palindromes
print("List of palindromes", listIsPalindrome(l))