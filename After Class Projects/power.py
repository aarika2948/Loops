#Take the input for n 
n=int(input("Enter the number="))
x=int(input("Enter the power="))
#Give the condition
result=1
for i in range(1, x+1):
    result*=n
print(result)
