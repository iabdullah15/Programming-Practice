def times_table(n):

    for y in range(1, n+1):

        for x in range(1, n+1):

            print(x * y, end='\t')
            
        print('')
            
times_table(5)