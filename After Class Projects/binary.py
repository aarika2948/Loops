n=int(input("Enter the number which you want to convert="))
temp=n
b_1=[]
while temp>0:
    digit=temp%2
    b_1.append(digit)
    temp=temp//2
b_2=b_1[::-1]
print(b_2)
final=0
for b in b_2:
    final=(final*10)+b
print(f"The binary digit for {n} is {final}")