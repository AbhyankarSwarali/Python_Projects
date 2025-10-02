import random

COLORS = ['R', 'G', 'Y', 'B', 'W', 'O']
TRIES = 10
CODE_LEN = 4

def generate_code():
    code = []

    for _ in range(CODE_LEN):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():

    while True:
        guess = input("Guess: ").upper().split(' ')

        if len(guess) != CODE_LEN:
            print(f"You must guess {CODE_LEN} colours.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid colour: {color}")
                print('Try again')
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print("Welcome to Colour Code")
    print(f"You have {TRIES} to guess the correct code...")
    print(f"You mmust guess among: ", *COLORS)


    code = generate_code()
    for attempts in range(1, TRIES +1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LEN:
            print(f"You guessed the code in {attempts} tries.")
            break

        print(f"Correct positions: {correct_pos}")
        print(f"Incorrect positions: {incorrect_pos}")

    else:
        print(f"You ran out of tries.")
        print("The correct code is: ", *code)


if __name__ == "__main__":
    game()