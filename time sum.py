def formart_(x):
    if x<10:
        return("0"+str(x))
    else:
        return(str(x))
x=input()
if x=="":
    print("error")
else:
    ta=[x]
    while x!="":
        x=input()
        if x!="" :
            ta.append(x)
print(ta)
s=0
h=0
for i in range(len(ta)):
    e=ta[i].split(":")
    h=h+int(e[1])
    s=s+int(e[0])
t=str(s+h//60)+":"+formart_(h%60)

print(t)