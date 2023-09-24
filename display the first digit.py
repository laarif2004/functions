def first_digit(x):
    test=False
    if x//10==0:
        test=True
    else:
        while test==False:
            x=x//10
            if x//10==0:
                test=True
    return(x)
