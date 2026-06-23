lower=int(input("Enter the beginning of the range="))
upper=int(input("Enter the ending of the range="))
for num in range(lower, upper+1):
    if num>1:
        for i in range(2, num):
            if (num%i==0):
                break
        else:
            print(num) 
