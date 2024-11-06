def settify(l: list):

    new_l = []

    for x in l:

        if x not in new_l:

            new_l.append(x)
        else:
            continue

    return new_l


print(settify([1, 2, 3, 2, 1, 3, 4, 5, 6, 1, 2, 2, 1, 3, 7, 8, 9]))
