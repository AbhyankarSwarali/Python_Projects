# 🎲 Dice Rolling Game in Python
This is a simple and interactive Dice Rolling Game for 2 to 4 players built using Python. The game simulates players taking turns to roll a die, accumulating scores—unless they roll a 1, which ends their turn! The first player to reach a score above 50 wins the game.

## 🕹️ How to Play
- The game begins by asking for the number of players (between 2 and 4).
- On each player's turn, they can choose to roll the die.
- If the die rolls 1, their turn ends and they lose any points accumulated in that round, but if they roll 2–6, the number is added to their current score.
- The player can keep rolling to accumulate more points or stop voluntarily to save their score.
- The first player to cross 50 points wins.

## 🧠 Game Logic Overview
Here's a quick look at how the game operates:

```python                           Copy code
if Value == 1: 
    print('You rolled a 1! Your turn is over')
    current_score = 0
    break
else: 
    current_score += Value
    print('You rolled: ', Value)
```
If a player rolls a 1, their turn ends and the score for that turn is lost. Any other value is added to their score. Strategic risk-taking is key!

## ✅ Features
* Simple CLI-based game.
* Supports 2 to 4 players.
* Keeps track of individual player scores.
* Displays real-time updates during gameplay.
* Ends automatically when a player scores above 50.

## ▶️ How to Run
1. Make sure you have Python installed (version 3+).
2. Clone the repository:
```bash                              Copy code
git clone https://github.com/yourusername/dice-rolling-game.git
cd dice-rolling-game
```
3. Run the script:
```bash                              Copy code
python dice_game.py
```

## 💡 Example Gameplay
```vbnet                             Copy code
Enter number of players (2-4): 3

Player number 1's turn
Your total score is: 0

Would you like to roll (y)?: y
You rolled: 5
Your score is: 5

Would you like to roll (y)?: y
You rolled: 1! Your turn is over
Your total score is: 0
```

## 📁 File Structure
```                                  Copy code
dice-rolling-game/
├── dice_game.py
└── README.md
```

## 📜 License
This project is licensed under the MIT License.

## Thank you ! Enjoy the game.
