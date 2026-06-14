print("The rides availible are:\n 1)Bike \n 2)Car")
choice_1=int(input("Enter the corresponding serial no.="))
if (choice_1==1):
    print("The subcategories for a bike are:\n1)Scooty\n2)Motorcycle")
    choice_2=int(input("Enter the corresponding serial no. ="))
    if (choice_2==1):
        print("You have chosen a Scooty.")
    elif (choice_2==2):
        print("You have chose a Motorcycle.")
    else:
        print("Invalid Input")
elif(choice_1==2):
    print("The subcategories for a car are:\n1)Sedan\n2)SUV")
    choice_3=int(input("Enter the corresponding serial no. ="))
    if (choice_3==1):
        print("You have chosen a Sedan.")
    elif (choice_3==2):
        print("You have chosen an SUV.")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")
    