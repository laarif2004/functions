def binary_test(x):
    test=True
    while x!=0 and test:
        if (x%10)!=0 and (x%10)!=1:
            test=False
        else:
            x=x//10
    return(test)
