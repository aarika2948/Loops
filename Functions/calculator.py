def add(x, y):
    sum=x+y
    return sum
def sub(x, y):
    diff=x-y
    return diff
def pro(x, y):
    product=x*y
    return product
def div(x, y):
    quotient=x/y    
    return quotient
print(" \n a:add \n b:subtraction \n c:multiplication \n d:division")
choice=input("Enter the operation (a/b/c/d)=").lower()
num_1=float(input("Enter the first number="))
num_2=float(input("Enter the second number="))
if choice=="a":
    print(num_1,"+", num_2, "=", add(num_1, num_2))
elif choice=="b":
    print(num_1,"-", num_2, "=", sub(num_1, num_2))
elif choice=="c":
    print(num_1,"*", num_2, "=", pro(num_1, num_2))
elif choice=="d":
    print(num_1,"/", num_2, "=", div(num_1, num_2))
else:
    print("Invalid Input")



