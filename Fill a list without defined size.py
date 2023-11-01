a=[]
e=input()
if e=="stop":
    print(a)
else:
    a=[int(e)]
    while e!="stop":
        e=input()
        if e!="stop":
            a.append(int(e))
print(a)
        
        
