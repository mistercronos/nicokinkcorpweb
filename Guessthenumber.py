import random
class bcolors:
    Red = '\033[91m'
    Blank = '\033[0m'
    Green = '\033[92m'
x = random.randint(0, 100)
tnw = "The number was: "
tries = 8
ans = 11
yes = 'yes'
print("this is a game in which you will use your intelligence")
print("Welcome to NicoMatt's Guessing game! This is a game where you must guess a number between 0 and 100 (There are clues!)")
start = input("Start? (No capitals) ")
if start == yes:
    while ans != x:
        ans = input("Try to guess a number between 0 and 100 ")
        if ans == x:
            print bcolors.Green + ("You got it!")
            print("Well done!")
        elif ans > 100:
            print("Sorry, that number is not between 0 and 100")
            tries = tries + 1
        elif ans > x:
            print("Too big")
        elif ans < x:
            print("Too small")
        tries = tries - 1
        if tries == 0:
            print bcolors.Red +("You are out of tries")+ bcolors.Blank
            print(tnw)
            print(x)
            ans = x
else:
    print("ByeBye!")