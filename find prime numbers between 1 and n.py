n=int(input())
a=""
for i in range(1,n+1):
    e=0
    for j in range(1,i+1):
        if i%j==0:
            e=e+1
    if e==2:
        a=a+str(i)+","
print(a)
        