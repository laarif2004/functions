#list contains tuples of different size, element types
#the programe ignores any non numeric elements
l=[(1,7,"a",10),(3,5,"a",8),(2,2,True,3,1)]
t=()
def longest(l):
    max=len(l[1])
    for x in l:
        if len(x)>max:
            max=len(x)
    return(max)
for i in range(longest(l)):
    s=0
    for x in l:
        if len(x)>i:
            if str(x[i]).isnumeric():
                s=s+x[i]
    t+=(s,)
print(t)
