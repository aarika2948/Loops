#The title of the project and the story line weren't matching so I created a programme which integrates both the ideas
n=int(input("Enter the no.="))
temp=n
count=0
rev=[]
while temp>0:
    r=temp%10
    rev.append(r)
    count+=1
    temp=temp//10
re=0
final=0
for re in rev:
    final=(final*10)+re
print(f"The reversed integer of {n} is {final}")
print(f"The length of the integer {n} is {count}")
    

