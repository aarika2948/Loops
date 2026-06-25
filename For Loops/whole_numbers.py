#Take the input of the number
n=int(input("Enter the number="))
#Declare the variable
sum=0
#Give the loop
for i in range(1, n+1):
    sum+=i
    print(f"The sum with {i} is {sum}.")
print(f"The final sum is {sum}.")