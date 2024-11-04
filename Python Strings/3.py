'''
3. Count Vowels and Consonants
Count Vowels and Consonants
Input: "Hello, World!"
Output: Vowels: 3, Consonants: 7
'''

def count_vowelsAndConsonants(inputStr: str):

    vowels = 0
    consonants = 0
    for char in inputStr:
        
        if ord(char) in [41, 45]:
            vowels+=1
    
    print(vowels)    

count_vowelsAndConsonants('Hello, World')