import random

num = random.randint(1,9)
while(True):
    guess = int(input("Guess the number: "))
    if guess==num:break
    elif guess>num:
        print("Guess lower")
    else:
        print("Guess higher")
print("Right on")