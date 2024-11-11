def isPalindrome(s: str):
    
    s2 = ''.join(list(reversed(s)))
    return s == s2

# List of palindrome strings
palindromes = ["racecar", "level", "madam", "rotor", "civic", "radar", "deified", "noon", "refer", "wow"]

# List of non-palindrome strings
non_palindromes = ["apple", "banana", "computer", "house", "table", "garden", "mountain", "school", "flower", "window"]

l = palindromes + non_palindromes

palindrome_list = [s for s in l if isPalindrome(s)]
print(palindrome_list)