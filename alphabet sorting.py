def permut(x,y):
    a=x
    x=y
    y=a
    return(x,y)
def sort(t):
    test=False
    while test==False:
        test=True
        for i in range(len(t)-1):
            if t[i+1][0].upper()==t[i][0].upper():
                if t[i+1]<t[i]:
                    t[i+1],t[i]=permut(t[i+1],t[i])
                    test=False
            elif t[i+1].upper()<t[i].upper():
                t[i+1],t[i]=permut(t[i+1],t[i])
                test=False
    return(t)
x=input("enter name or enter nothing to cancel")
if x=="":
    print("error")
else:
    a=[x]
    while x!="":
        x=input()
        if x!="" :
            a.append(x)
    print(a)
    print(sort(a))