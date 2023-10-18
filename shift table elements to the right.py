import numpy as np
def shift(t,n,e):
    for i in range(e):
        x=t[n-1]
        for i in range(n):
            t[n-1-i]=t[n-2-i]
        t[0]=x
    return(t)
n=int(input("Table size: "))
t=np.array([int]*n)
for i in range(n):
    t[i]=int(input("T["+str(i)+"]= "))
e=int(input("Shift by how many numbers? "))
print(t)
print(shift(t,n,e))