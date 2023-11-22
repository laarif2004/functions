def bin(x):
    if x==0:
        return(0)
    else:
        a=""
        while x!=0:
            a=str(x%2)+a
            x=x//2
    return(int(a))
def decimal(x):
    a=0
    for i in range(len(str(x))):
        a=a+(x%10)*2**i
        x=x//10
    return(a)
def bcd_dec(x):
    x=x.split(" ")
    test=True
    for a in x:
        if decimal(int(a))>9:
            test=False
    if test==False:
        return("Error")
    else:
        a=""
        for i in range(len(x)):
            a=a+str(decimal(int(x[i])))
        return(int(a))
e=input("Write in xxxx xxxx form: ")
print(bcd_dec(e))
        
        