marks=int(input("enter the value" ))
if  marks<40:
    print(marks, "sorry you are failed")
elif marks>=40 and marks<50:
    print(marks, "you are just pass")
elif marks>=50 and marks<60:
    print(marks, "average" )
elif marks>=60 and marks<70:
    print(marks,"above average")
elif marks>=70 and marks<80 :
    print(marks,"distinction")
elif marks>=80 and marks<=100:
    print(marks,"toppers category")
else :
    print(marks,"please enter a valid number")
