# Speed Typing Test

A simple speed typing test built in Python using the curses module.
This program measures your Words Per Minute (WPM) as you type a randomly chosen sentence from a text file.

## 🖥️ About curses

The curses module is a Python library for creating **text-based user interfaces (TUIs)** inside the terminal.
Instead of just printing plain text, curses gives you powerful tools to:
- Move the cursor to any position on the screen
- Detect individual key presses (without waiting for Enter)
- Apply colors, highlighting, and formatting
- Redraw parts of the screen dynamically
- Build interactive applications like editors, dashboards, or games
- In this project, curses is used to:
  * Clear and refresh the screen each time you type
  * Highlight correct characters in green and mistakes in red
  * Capture real-time keystrokes for a smooth typing experience
  * Display the live WPM counter at the top

## ⚠️ Note for Windows users: 
Python does not include curses by default on Windows. 
You need to install windows-curses with:
```
pip install windows-curses
```

## ✨ Features
- Displays a welcome screen before starting
- Loads random sentences from a file (test_text.txt)
- Tracks your WPM in real-time
- Highlights correct/incorrect characters
- Supports **Backspace** to fix mistakes
- Ends automatically when you finish typing
- Press **Esc** anytime to exit

## ⚠️ Note for text document:
The text document with typing sentences must be present in the same directory as of the python code.

## 📦 Requirements
- Python 3.6+
- curses (preinstalled on Linux/macOS, install windows-curses on Windows)

## ▶️ Usage
- Clone or download the project.
- Create a test_text.txt file with sentences (one per line). Example:
```
The quick brown fox jumps over the lazy dog
Speed typing tests help improve accuracy and speed
Python is a fun programming language to learn
```
- Run the script inside **command prompt**:
```
python speed_typing.py
```

## 🎮 Controls
- **Enter** → Start the test
- **Backspace** → Delete last typed character
- **Esc** → Exit at any point

## 📝 Example Run
```
Welcome to the Speed Typing test
Press 'Enter' to begin
```
- Typing begins with a live WPM counter until you finish.
- After completion, you’ll see:
```
You completed the test. Press any key to continue...
```

## Flex your typing skills here...
## Happy Learning





