def reverse_str(s: str):
    
    if s == '':
        return ''
    
    return reverse_str(s[1:(len(s)+1)]) + s[0]


s = 'hello'
print(reverse_str(s))