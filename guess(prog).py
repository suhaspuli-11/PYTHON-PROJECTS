import random

num = int(input("Enter a number between 0 and 9: "))
lo,hi,total = 0,9,0
while(True):
    guess = random.randint(lo,hi)
    print(guess)
    if guess==num:
        break
    elif guess>num:
        print("Guess lower!")
        hi=guess
    else:
        lo=guess+1
        print("Guess higher")
    total += 1
print("Right on!")
print(f"You only took {total} number of guesses!")