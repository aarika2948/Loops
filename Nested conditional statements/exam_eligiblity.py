medical=input("Enter Y if you have a medical condition and N if not =").upper()
if (medical=="Y"):
    print("You are eligible to give the exam.")
elif (medical == "N"):
    att=int(input("Enter you attendence percent ="))
    validRange=range(1,101)
    if att not in validRange:
        print("Invalid Input")
    else:
        if (att>=75):
            print("You are eligible to give the exam.")
        else:
            print("You are not eligible to give the exam.")
else:
    print("Invalid  Input")