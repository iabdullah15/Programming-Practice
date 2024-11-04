'''
2.
Palindrome Check
Check if a given string is a palindrome (reads the same forward and backward).
Input: "racecar"
Output: True
'''
def reverse_str(inputStr: str) -> str:
    
    return inputStr[::-1]
    


def isPalindrome(inputStr: str) -> bool:

    reversed_str = reverse_str(inputStr)
    
    return reversed_str == inputStr


myString = 'civic'
print(isPalindrome(myString))