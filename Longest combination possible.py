def long_chain(t):
    b=[]
    z=[]
    sub=0
    a=0
    for k in range(len(t)):
        for i in range(k,len(t)):
            max=[t[k]]
            if t[i]>t[k]:
                a=t[i]
                max.append(t[i])
                for j in range(i,len(t)):
                    if t[j]>a:
                        a=t[j]
                        max.append(t[j])
                    if j+1==len(t):
                        b.append(max)
                        if len(max)>sub:
                            sub=len(max)
    for i in range(len(b)):
        if len(b[i])==sub:
            z.append(b[i])
    return(z)
#Main Program
t=[]
n=int(input("Give array size: "))
for i in range(n):
    x=int(input())
    t.append(x)
print(t)
print(long_chain(t))
