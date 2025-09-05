import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {'A':2, 'B':4, 'C':6, 'D':8}
symbol_value = {'A':5, 'B':4, 'C':3, 'D':2}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        won = True
        for column in columns:
            if column[line] != symbol:
                won = False
                break
        if won: 
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines

def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, sym_count in symbols.items():
        for _ in range(sym_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], '|', end=' | ')
            else:
                print(column[row], end='')

        print()



def deposit():
    while True:
        amount = int(input("Enter deposit amount: Rs."))
         
        if amount > 0:
            break
        else: 
            print("Amount must be greater than 0")

    return amount

def no_of_lines():
    while True:
        lines = int(input("Enter number of lines (1-3) you want to bet on: "))

        if 1 <= lines <= MAX_LINES:
            break
        else:
            print("Enter valid number of lines")

    return lines

def get_bet():
    while True:
        amount = int(input("How much would you like to bet on each line?"))
         
        if MIN_BET <= amount <= MAX_BET:
            break
        else: 
            print(f"Amount must be between Rs.{MIN_BET} and Rs.{MAX_BET}")

    return amount

def spin(balance):
    lines = no_of_lines()

    while True: 
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("Not enough balance to bet")
        else: 
            break


    
    print(f'You are betting Rs.{bet} on {lines} lines')
    print(f'Total bet is equal to Rs.{total_bet}')
    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won Rs.{winnings}')
    print(f'You won on ', *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True: 
        print(f'Current balance: Rs.{balance}')
        answer = input("Press enter to play or q to quit")

        if answer == 'q':
            break
        balance += spin(balance)

    print(f'You are left with Rs.{balance}')
    



main()