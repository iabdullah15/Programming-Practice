# 1.
# Reverse a String
# Write a function to reverse a string without using any built-in reverse methods.

def reverse_string(input: str):
    
    reversed_str = []
    for i in range((len(input)-1), -1, -1):
        reversed_str.append(input[i])

    return ''.join(reversed_str)
    

myStr = 'Abdullah'
reversed_str = reverse_string(myStr)
print('Reversed str:', reversed_str)