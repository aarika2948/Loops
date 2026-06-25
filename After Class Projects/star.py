rows=int(input("Enter the number of rows you want="))
middle=rows//2
spaces=rows-1
star=0
for i in range(1, rows+1):
    for s in range(spaces):
        print(" ", end=" ")
    for n in range(star+1):
        print("*", end=" ")
    print()
    star+=1
    spaces-=1