def zip(l1: list, l2: list):

    if len(l1) != len(l2):
        raise ValueError("Length of lists are not the same")

    l = []
    for i in range(len(l1)):

        t = (l1[i], l2[i])
        l.append(t)

    return tuple(l)


def dict(i: iter):

    d = {}
    
    for x in i:
        # d.update({x[0]: x[1]})
        d[x[0]] = x[1]

    return d


t = dict(zip([1, 2], ['one', 'two']))
print(t)
