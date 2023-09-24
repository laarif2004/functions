def binary(x):
    a=""
    while x!=0:
        a=str(x%2)+a
        x=x//2
    return(int(a))
