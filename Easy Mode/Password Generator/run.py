'''
options
 -> Length
 -> Toggle
    -> Symbols (5%) -> 5 -> 1
    -> Numbers (15%) -> 15 -> 3
    -> Alphabets (80%) -> 80 -> 16
 -> Generate and Store
'''

from random import randint

choice = None
symbolsAllowed = True
numbersAllowed = True
alphabetsAllowed = True
lenght = 20

symbolArr = ['#','@','&', '%', '_', "?"]
alphabets = 'qwertyuiopasdfghjklzxcvbnm'
capsAlpha = alphabets.upper()

alphabetsArr = list(alphabets)
capsAlphaArr = list(capsAlpha)

def options():
    global choice
    print("1. Generate\n2. Settings\n0. Exit")
    choice = int(input())
    if choice >= 3:
        print("---- Choose a valid option ----")
        options()

def generatePassword():
    temp = ""
    if symbolsAllowed and numbersAllowed and alphabetsAllowed:
        for i in range(lenght):
            # 20 (16, 3, 1)
            dec = randint(1, 20)
            if(dec <= 2):
                rand = randint(0,(len(symbolArr)-1))
                temp += symbolArr[rand]
                continue
            elif(dec <= 5 and dec >= 3):
                rand = randint(0,9)
                temp += str(rand)
                continue
            elif(dec >= 6 and dec <= 13):
                rand = randint(0, len(alphabetsArr)-1)
                temp += capsAlphaArr[rand]
                continue
            else:
                rand = randint(0, len(alphabetsArr)-1)
                temp += alphabetsArr[rand]
                continue
    elif symbolsAllowed and alphabetsAllowed:
        for i in range(lenght):
            # 20 (16, 3, 1)
            dec = randint(1, 20)
            if(dec <= 2):
                rand = randint(0,(len(symbolArr)-1))
                temp += symbolArr[rand]
                continue
            elif(dec <= 5 and dec >= 3):
                rand = randint(0,9)
                temp += str(rand)
                continue
            elif(dec >= 6 and dec <= 13):
                rand = randint(0, len(alphabetsArr)-1)
                temp += capsAlphaArr[rand]
                continue
            else:
                rand = randint(0, len(alphabetsArr)-1)
                temp += alphabetsArr[rand]
                continue
    
    temp += "\n"
    f = open("passwords.txt", "a")
    f.write(temp)
    f.close()


while choice != 0:
    options()
    if(choice == 1):
        generatePassword()
else:
    print("Thanks for using!")