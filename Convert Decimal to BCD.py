def bin(x):
    if x==0:
        return(0)
    else:
        a=""
        while x!=0:
            a=str(x%2)+a
            x=x//2
    return(int(a))
def for_mat(x):
    for i in range(abs(len(str(x))-4)):
        x="0"+str(x)
    return(str(x))
def bcd(x):
    a=""
    for i in range(len(str(x))):
        a=for_mat(bin(x%10))+" "+a
        x=x//10
    return(a)
a=int(input("Give a decimal number: "))
print(bcd(a))

