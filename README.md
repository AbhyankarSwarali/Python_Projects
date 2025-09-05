# 🎰 Slot Machine Game (Python)

This is a simple **command-line slot machine game** written in Python.  
The player deposits money, chooses the number of lines to bet on, sets a bet amount, and spins the slot machine.  
Winnings are calculated based on matching symbols in a row.

---

## 🚀 Features
- Deposit money to start playing
- Bet on **1 to 3 lines**
- Adjustable bet per line (min: Rs.1, max: Rs.100)
- Random slot machine spin with different symbol probabilities
- Payouts based on symbol values
- Keeps track of player balance across multiple spins

---

## 🎲 Rules
1. The slot machine has **3 rows × 3 columns**.
2. Symbols:
   - `A` → Value 5 (rare)
   - `B` → Value 4
   - `C` → Value 3
   - `D` → Value 2 (most common)
3. You win if **all symbols in a row match**.
4. Winnings = `Symbol Value × Bet Amount`.
5. Game continues until you quit or run out of balance.

---

## 📂 Project Structure

slot_machine.py   # Main Python file (game logic)
README.md         # Documentation

---

## ▶️ How to Run
1. Clone or download the repository.
2. Make sure you have **Python 3.x** installed.
3. Run the game:
   ```bash
   python slot_machine.py
```

Example Gameplay:
Enter deposit amount: Rs.100
Enter number of lines (1-3) you want to bet on: 3
How much would you like to bet on each line?10
You are betting Rs.10 on 3 lines
Total bet is equal to Rs.30
A | B | D
B | B | B
C | A | C
You won Rs.40
You won on 2
Current balance: Rs.110

⚠️ Note

This project is for learning purposes only and does not involve real money.

