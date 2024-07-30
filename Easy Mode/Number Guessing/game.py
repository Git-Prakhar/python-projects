from random import randint

diff = 0
choice = None
diffLang = [5, 10, 20]

def setDiff():
    global diff
    print(f"1. for range 1-{diffLang[0]}\n2. for range 1-{diffLang[1]}\n3. for range 1-{diffLang[2]}\n0. for back")
    code = int(input())
    if(code == 0): return
    diff = code - 1
    return

def gameStart():
    print(f"Guess a number between 1-{diffLang[diff]} : ", end="")
    player = int(input())
    cpu = randint(1,diffLang[diff])
    if(player == cpu):
        print(f"You guessed the correct number!\nCPU : {cpu} | Your : {player}")
    else:
        print(f"BOO! You are wrong! Try again?\nCPU : {cpu} | Your : {player}")
    return

def options():
    global choice
    print("1. Guess\n2. Set Difficulty\n0. Exit")
    choice = int(input())

while(choice != 0):
    options()
    if(choice == 1):
        gameStart()
    elif choice == 2:
        setDiff()
else:
    print("Thanks for playing!")