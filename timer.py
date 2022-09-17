import time

# The countdown function is defined below

def countdown(t):
    while t:
        minutes, seconds = divmod(t, 60)
        timer2 = f"{minutes:{0}{2}}:{seconds:{0}{2}}"
        print(timer2, end="\r")
        time.sleep(1)
        t -= 1
    print('It\'s time!')

t = int(input("Enter the time in seconds: "))
countdown(t)