def myFun(**kwargs):
    
    print(type(kwargs))
    print(kwargs)
    # for key, value in kwargs.items():
    #     print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')