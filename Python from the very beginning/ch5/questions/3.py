def histogram(l: list):

    frequency = 0
    l.sort()
    new_l = []

    print("Element  Frequency")

    for i in range(len(l)):
        
        if l[i] not in new_l:
            
            new_l.append(l[i])
            frequency+=1
            for j in range(i+1, len(l)):

                if l[i] == l[j]:
                    frequency += 1

            print(f"    {l[i]}        {frequency}")
            frequency = 0


histogram(['f', 'b', 'h', 'c', 'a', 'e', 'j', 'd', 'g', 'h', 'i', 'e', 'a', 'g', 'd', 'i', 'b', 'f', 'c', 'j', 'a', 'd', 'e', 'f', 'g', 'b', 'h', 'i', 'j', 'e', 'c', 'b', 'h', 'a'])
