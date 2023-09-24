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
a=int(input())
e=first_digit(a)
print(e,a)