#Take input of num from the user
num=int(input("Enter the number="))
temp=num
string=str(temp)
x=len(string)
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**x
    temp=temp//10
if sum==num:
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number.")
