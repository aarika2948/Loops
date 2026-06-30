import random
secret=random.randint(1, 51)
lives=5
print("You have 5 lives.")
tens=secret//10
n=tens*10
n_1=(tens+1)*10
while lives>0:
    num=int(input("Enter your guess="))
    if num==secret:
        print(f"{num} is the correct guess.")
        break
    elif num in range(secret+1, 51):
        print(f"You should try going lower than {num} but higher than {n}")
    elif num in range(1, secret):
        print(f"You should try going going higher than {num} but lower than {n_1}")
    else:
        print(f"{num} is not in the valid range.")
    lives-=1
    print(f"You have {lives} lives left.")
else:
    print("You have no lives left.")
    print(f"{secret} was the number")