def binary(x):
    if x==0:
        return(0)
    else:
        a=""
        while x!=0:
            a=str(x%2)+a
            x=x//2
        return(int(a))
