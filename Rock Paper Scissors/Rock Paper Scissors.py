import random

item = ['Rock', 'Paper', 'Scissor']

user = input("Enter your move (Rock/Paper/Scissor): ")
comp = random.choice(item)

if user == comp: 
    print("Your choice: ", user)
    print("Computer's choice: ", comp)
    print(' ')
    print("Match tie")

elif user == item[0] and comp == item[1]:
    print("Your choice: ", user)
    print("Computer's choice: ", comp)
    print(' ')
    print("Paper beats Rock")
    print('You lose')

elif user == item[0] and comp == item[2]:
    print("Your choice: ", user)
    print("Computer's choice: ", comp)
    print(' ')
    print("Rock beats Scissors")
    print('You win')

elif user == item[1] and comp == item[0]:
    print("Your choice: ", user)
    print("Computer's choice: ", comp)
    print(' ')
    print("Paper beats Rock")
    print('You win')

elif user == item[1] and comp == item[2]:
    print("Your choice: ", user)
    print("Computer's choice: ", comp)
    print(' ')
    print("Scissors beat Paper")
    print('You lose')

elif user == item[2] and comp == item[0]:
    print("Your choice: ", user)
    print("Computer's choice: ", comp)
    print(' ')
    print("Rock beats Scissors")
    print('You lose')

elif user == item[2] and comp == item[1]:
    print("Your choice: ", user)
    print("Computer's choice: ", comp)
    print(' ')
    print("Scissors beat Paper")
    print('You win')