# 🐢 Turtle Racing Game

A fun Python game built with the turtle graphics library. Multiple turtles race against each other, and the program declares a winner at the end. Along with fun explore the uses of various modules and libraries pre-defined in Python.

## 📌 Features

Choose 2 to 10 racers.

Turtles are assigned random colors.

Each turtle moves forward a random distance each turn.

Game ends automatically when a turtle crosses the finish line.

Window auto-closes after announcing the winner.

🚀 How to Run

Make sure you have Python 3.x installed.

Save the script as turtle_race.py.

Run the game:

python turtle_race.py


Enter the number of racers when prompted (between 2 and 10).

🖼️ Game Window

The race window opens with all turtles aligned at the bottom.

They move upwards randomly until one reaches the top.

Winner’s color is printed in the console.

⚙️ Requirements

Python 3.x

No extra libraries required (uses built-in turtle and random).

🎮 Example Gameplay
Enter number of racers (2 - 10): 5
The winner is green turtle !!

🛠️ Customization

Change COLORS list to add/remove turtle colors.

Change turtle shape in create_turtle() (racer.shape('turtle')) to 'arrow', 'circle', etc.

Adjust race speed by modifying the random distance range:

distance = random.randrange(1, 20)

📜 License


Free to use, modify, and share for fun and learning. 🎉
