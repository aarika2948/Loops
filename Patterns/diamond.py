rows=int(input("Enter the number of rows you want="))#7
if rows%2==0:
    middle=rows//2 #4
else:
    middle=(rows//2)+1
spaces=middle-1 #3
for i in range(1, middle+1): #range(1, 5)
    for s in range(spaces):
        print(" ", end="")
    number=1
    for n in range(2*i-1): #2*1 -1 = 1
        print(number, end="")
        number+=1
    print()
    spaces-=1
spaces=1
for i in range(1, middle): #range(1, 4) = i=1
    for s in range(spaces):
        print(" ", end="")
    number=1
    for n in range(1, 2*(middle-i)): #range(1, 6)
        print(number, end="")
        number+=1
    print()
    spaces+=1
