# 🎨 Colour Code
A simple Mastermind-inspired code-breaking game built with Python. The goal is to guess the secret sequence of colours within a limited number of tries.

##  How It Works
- The program randomly generates a code consisting of 4 colours from:
```
R, G, Y, B, W, O
- R = Red
- G = Green
- Y = Yellow
- B = Blue
- W = White
- O = Orange
```
- You have 10 tries to guess the code.
- For each guess, the program provides feedback:
- **Correct positions** → Number of colours in the right position.
- **Incorrect positions** → Number of correct colours but in the wrong position.
- If you guess all 4 colours in the correct order, you win 🎉.
- If you run out of tries, the correct code is revealed.

##  Run the Game
- Clone or Download
```
git clone https://github.com/yourusername/colour-code-game.git
cd colour-code-game
```
- Run the script
```
python colour_code.py
```

## Example Gameplay
```
Welcome to Colour Code
You have 10 to guess the correct code...
You must guess among: R G Y B W O

Guess: R G Y B
Correct positions: 1
Incorrect positions: 2

Guess: R W O G
Correct positions: 0
Incorrect positions: 3

Guess: R B Y O
You guessed the code in 3 tries.
```

## Requirements
- Python 3.x
- No external libraries needed (uses only random)

## Happy gaming
## Happy Learning!!
