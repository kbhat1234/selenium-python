high_income = False
good_credit = False
student = False

if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not Eligible")

if high_income or good_credit or not student:
    print("Eligible")
else:
    print("Not Eligible")

if (high_income and good_credit) or not student:
    print("Eligible")
else:
    print("Not Eligible")


age = 1
if age >= 18 and age < 65:
    print("Eligible for loans")
else:
    print("Not Eligible for loans")

if 18 <= age < 65:
    print("Eligible for loans")
else:
    print("Not Eligible for loans")