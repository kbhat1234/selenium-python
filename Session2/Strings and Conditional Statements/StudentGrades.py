marks = int(input("Enter the marks: "))

if (marks >= 90):
    grade = "A"
    print(f'Grade is {grade}')
elif (marks < 90 and marks >= 80):
    grade = "B"
    print(f'Grade is {grade}')
elif (marks < 80 and marks >= 70):
    grade = "C"
    print(f'Grade is {grade}')
else:
    grade = "D"
    print(f'Grade is {grade}')