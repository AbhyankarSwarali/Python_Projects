# Number Guessing Game 🎲

This is a simple Python program where the computer randomly selects a
number between **1 and 10**, and the player has to guess it within a
limited number of attempts.

## 📌 Features

-   Random number generation between **1 and 10**.\
-   User gets **4 attempts** to guess the number.\
-   Hints provided after each wrong guess:
    -   `"Your guess is smaller"` if the guess is less than the number.\
    -   `"Your guess is bigger"` if the guess is greater than the
        number.\
-   If guessed correctly, the game congratulates the player.\
-   If all attempts are used, the game reveals the correct number.

## 🖥️ How to Run

1.  Make sure Python is installed (Python 3.x recommended).\

2.  Save the code in a file, for example:

    ``` bash
    number_guess.py
    ```

3.  Run the program in the terminal/command prompt:

    ``` bash
    python number_guess.py
    ```

## 🎮 Sample Gameplay

    Enter your guess: 5
    Your guess is smaller
    Enter your guess: 8
    Your guess is bigger
    Enter your guess: 7
    Correct guess!

Or, if all your attempts are used:

    Enter your guess: 2
    Your guess is smaller
    Enter your guess: 9
    Your guess is bigger
    Enter your guess: 7
    Your guess is smaller
    You used all your attempts. Try again later
    The correct number is:  8

## 📂 File Structure

    number_guess.py   # Main Python script
    README.md         # Documentation

## 🚀 Future Improvements

-   Allow user to set difficulty level (easy, medium, hard).\
-   Add option to play again without restarting the program.\
-   Keep track of number of games won/lost.
