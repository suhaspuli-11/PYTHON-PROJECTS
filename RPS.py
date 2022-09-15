import random

#Rock,paper&scissor game
#rock>scissor>paper>rock

def start():

    options = ['rock','paper','scissor']
    p1 = 'system'
    p2 = input("Enter player name: ")
    ch = 'y'
    total = one = two = 0

    while ch == 'y':

        print(f"Go!-->Game number {total+1}")
        system = random.choice(options)
        user = input('Enter your move: ')
        print(f"{p1} rolled {system}")
        print(f"{p2} rolled {user}")

        if system==user:
            print("It's a tie!")

        elif check(system,user):
            print(f"{p1} wins the round!")
            one += 1

        else:
            print(f"{p2} wins the round!")
            two += 1

        ch = input("Do you want to go again?(y/n) ")
        total += 1
    summary(p1,p2,one,two,total)


def summary(p1,p2,one,two,total):

    print(f"Total number of games played {total}")

    if one>two:
        print(f"{p1} is the winner with a winning count of --> {one}") 
        print(f"{p2} lost with {two} rounds won")
        print(f"{total-one-two} rounds ended in a draw!")

    elif one<two:
        print(f"{p2} is the winner with a winning count of --> {two}")
        print(f"{p1} lost with {one} rounds won")
        print(f"{total-one-two} rounds ended in a draw!")

    else:
        print(f"The game tied with each winning {one} rounds")


def check(player,opponent):

    if (player == 'rock' and opponent == 'scissor') or (player == 'scissor' and opponent == 'paper') \
        or (player == 'paper' and opponent == 'rock'):
        return True


start()