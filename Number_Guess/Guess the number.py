import random

n=random.randint(1, 10)
attempt = 1
max_attempts = 4
guess = 0

while attempt < max_attempts:
    guess=int(input("Enter your guess: "))
    attempt+=1

    if guess<n:
        print("Your guess is smaller")
    elif guess>n:
        print("Your guess is bigger")
    else:
        print("Correct guess!")
        break

if attempt == max_attempts:
    print("You used all your attempts. Try again later")
    print("The correct number is: ",n)
