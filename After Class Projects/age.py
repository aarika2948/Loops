age=int(input("Enter your age="))
validRange=range(0,)
if (age<=20):
    if (age>=10):
        print("You are eligible to enroll.")
    elif age not in validRange:
        print("Invalid Input")
    else:
        print("You are not eligible to enroll.")
else:
    print("Invalid Input")