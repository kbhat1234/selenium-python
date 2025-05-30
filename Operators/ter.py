age = 17
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
print("Exit the program")

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

high_income = False
good_credit = False

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")