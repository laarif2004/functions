import numpy
def distinct(x,t,n):
    test=True
    i=0
    while test and i<n:
        if t[i]==x:
            test=False
        else:
            i=i+1
    return(test)
a=int(input("Table size: "))
t=numpy.array([int]*a)
for i in range(a):
    t[i]=int(input("t["+str(i)+"]="))
    while distinct(t[i],t,i)==False:
        t[i]=int(input("you have already written this number,try again please:"))
print(t)
