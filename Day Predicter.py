#This algorithm will predict the day after a defined number of passed days
day={"SUNDAY": 0, 'MONDAY': 1, "TUESDAY": 2,"WEDNESDAY": 3,"THURSDAY": 4,"FRIDAY":5,"SATURDAY": 6}
d=input("Which day is it today: ")
while d.upper() not in day:
    print("Invalid Day")
    d=input("Try again: ")
x=int(input("how many days: "))
result=(day.get(d.upper())+x)%7
print("After",x,"days It will be",list(day.keys())[result].title())