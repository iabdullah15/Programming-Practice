'''
Write a function histogram to print out a table of frequencies of the elementsin a list. 
You might use the setify function you have just written to help.
'''


def histogram(l: list):

    frequency = 0
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


histogram([1, 2, 3, 2, 1, 3, 4, 5, 6, 1, 2, 2, 1, 3, 7, 8, 9])
