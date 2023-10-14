from random import*
a=randint(1,100)
print("A number has been picked, guess it ! Attempts remaining: 5")
b=int(input())
#Only 5 attempts
c=1
while b!=a and c<5:
    c=c+1
    print("Attempts remaining:",(6-c))
    if b>a:
        print("Too high")
        b=int(input())
    else:
        print("Too low")
        b=int(input())
    
if b==a:
    print("it is",a,"you won!")
else:
    print("No.. it was",a,"Better luck next time")
    
    
    
    