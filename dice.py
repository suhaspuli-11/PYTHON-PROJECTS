import random

p1 = input("Enter name of player one: ")
p2 = input("Enter name of player two: ")

w1,w2,tot,ch=0,0,0,'y'

print("Begin the game!")

while ch=='y':
    print("Roll your die!")
    print(f"{p1}'s turn!")
    d1 = random.randint(1,6)
    print(f"{p1} rolled a {d1}")
    print(f"{p2}'s turn!")
    d2 = random.randint(1,6)
    print(f"{p2} rolled a {d2}")
    if d1>d2:
        print(f"{p1} wins this round")
        w1 += 1
    elif d1<d2:
        print(f"{p2} wins this round")
        w2 += 1
    else:
        print("It's a tie!")
    ch = input("Do you want to go again?(y/n) ")
    tot += 1


if w1>w2:
    print(f"{p1} is the winner with a winning count of {w1}")
elif w1<w2:
    print(f"{p2} is the winner with a winning count of {w2}")
else:
    print(f"The game tied with each winning {w1}")