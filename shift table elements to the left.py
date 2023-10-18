import numpy as np
def shift(t,n,e):
    for i in range(e):
        x=t[0]
        for i in range(n-1):
            t[i]=t[i+1]
        t[n-1]=x
    return(t)
n=int(input("size of the table: "))
t=np.array([int]*n)
for i in range(n):
    t[i]=int(input("T["+str(i)+"]= "))
e=int(input("shift by how many ? :"))
print(t)
print(shift(t,n,e))
