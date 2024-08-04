import random

choice = None
score = [0, 0]

with open('score.txt', 'r') as f:
    data = f.read()
    if data:
        score = list(map(int, data.split()))

def options():
    global choice
    print('1. Rock\n2. Paper\n3. Scissors\n0. Quit')
    choice = input('Enter your choice: ')
    if not(choice.isdigit()):
        print('Invalid choice. Please enter a number.')
        options()
    else:
        choice = int(choice)
        if choice < 0 or choice > 3:
            print('Invalid choice. Please enter a number between 0 and 3.')
            options()

print('Current score: Player {} - {} Computer'.format(score[0], score[1]))
options()
while choice != 0:
    computer = random.randint(1,3)
    if choice == computer:
        print('It\'s a tie!')
    elif choice == 1:
        if computer == 2:
            print('You lose!')
            score[1] += 1
        else:
            print('You win!')
            score[0] += 1
    elif choice == 2:
        if computer == 3:
            print('You lose!')
            score[1] += 1
        else:
            print('You win!')
            score[0] += 1
    elif choice == 3:
        if computer == 1:
            print('You lose!')
            score[1] += 1
        else:
            print('You win!')
            score[0] += 1
    print('Score: Player {} - {} Computer'.format(score[0], score[1]))
    with open('score.txt', 'w') as f:
        f.write(f'{score[0]} {score[1]}')
    
    options()
else:
    print(f'Final score: Player {score[0]} - {score[1]} Computer')