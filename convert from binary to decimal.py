def decimal(x):
    a=0
    i=0
    while x!=0:
        a=a+((x%10)*2**i)
        i=i+1
        x=x//10
    return(a)

