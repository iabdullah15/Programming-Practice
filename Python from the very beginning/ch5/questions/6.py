def clip(val: int):
    
    if val < 1:
        return 1
    elif val > 10:
        return 10
    else:
        return val
    
def clip_list(l: list[int]):
    
    l2 = map(clip, l)
    
    return list(l2)
        
        
l = [i for i in range(-4, 20, 2)]
print(clip_list(l))

