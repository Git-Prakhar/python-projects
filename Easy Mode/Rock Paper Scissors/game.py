import random


def options():
    print("1. For Rock\n2. For Paper\n3. For Scissors\n0. to Quit")


options()
choice = int(input("Enter Choice : "))

optionList = ["Rock", "Paper", "Scissors"]

score = [0,0]

while not (choice == 0):
    cpuChoice = random.randint(0, 2)
    print(f"You Choose : {optionList[choice-1]}")
    print(f"CPU Choose : {optionList[cpuChoice]}")

    if choice == 1 and cpuChoice == 0:
        print("Draw")
    elif choice == 1 and cpuChoice == 1:
        print("CPU got the point")
        score[1] = score[1] + 1
    elif choice == 1 and cpuChoice == 2:
        print("You got the point")
        score[0] = score[0] + 1
    elif choice == 2 and cpuChoice == 0:
        print("You got the point")
        score[0] = score[0] + 1
    elif choice == 2 and cpuChoice == 1:
        print("Draw")
    elif choice == 2 and cpuChoice == 2:
        print("CPU got the point")
        score[1] = score[1] + 1
    elif choice == 3 and cpuChoice == 0:
        print("CPU got the point")
        score[1] = score[1] + 1
    elif choice == 3 and cpuChoice == 1:
        print("You got the point")
        score[0] = score[0] + 1
    elif choice == 3 and cpuChoice == 2:
        print("Draw")
    else:
        print("Choose an option : ")
        options()


    print(f"Score : User {score[0]} : CPU {score[1]}")
    options()
    choice = int(input("Enter Choice : "))
else:
    print("Thanks for playing")
