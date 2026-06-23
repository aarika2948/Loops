number=int(input("Enter the number="))
temp=number
digit_count=0
while temp>0:
    digit_count+=1
    temp=temp//10
if digit_count>=4:
    middle=digit_count//2
    count=0
    while number>0:
        digit=number%10 #456
        if count==middle:
            middle_digit_1=digit
        elif count==middle-1:
            middle_digit_2=digit
        number=number//10
        count+=1
    print(f"The product of {middle_digit_1} and {middle_digit_2} is {middle_digit_1*middle_digit_2}")

    
    