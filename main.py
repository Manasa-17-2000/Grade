grade = int(input("enter the grade : "))

if grade >= 90:
    print(grade, "0")
elif grade >= 80:
    print(grade, "A+")
elif grade >= 70:
    print(grade, "A")
elif grade >= 60:
    print(grade, "B+")
elif grade >= 50:
    print(grade, "B")
elif grade < 50:
    print(grade, "no grade")
