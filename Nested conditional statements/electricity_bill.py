units=int(input("Enter the no. of units consumed by you="))
if units in range(0,50):
    tax=25
    charge=((2.60*units)+tax)
    print(f"Your electricity bill is Rs.{charge}")
elif units in range(50,100):
    tax=35
    charge=((units*3.25)+tax)
    print(f"Your electricity bill is Rs.{charge}")
elif units in range(100,200):
    tax=45
    charge=((units*5.26)+tax)
    print(f"Your electricity bill is Rs.{charge}")
elif (units>=200):
    tax=75
    charge=((units*8.45)+tax)
    print(f"Your electricity bill is Rs.{charge}")
else:
    print("Invalid Input")





    

