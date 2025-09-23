# 🏃‍♂️🧩 Maze Runner
This project is a simple **maze solver and visualizer** written in Python. It uses **Breadth-First Search (BFS)** to find the shortest path from a start point `O` to an end point `X` inside a maze.

The visualization is done using the **`curses`** library, so the path exploration is shown step by step in the terminal.

---

## 🧩 How it Works
1. The maze is represented as a 2D list of characters:
   - `#` → Wall  
   - ` ` (space) → Free path  
   - `O` → Start position  
   - `X` → End/Goal  

2. **BFS** is used to explore the maze:
   - At each step, the algorithm checks the neighboring cells (up, down, left, right).  
   - Explored cells are added to a queue until the goal `X` is found.  

3. The maze is drawn in the terminal using `curses`:
   - 🔵 Blue → Maze walls and open spaces  
   - 🔴 Red `X` → Current explored path  

---

## ▶️ Running the Code

### 1. Clone or Download
Save the file as `maze_runner.py`.

### 2. Run in a Real Terminal  
- **Important:** `curses` does not work well in VS Code’s integrated terminal.  
- You must run it in a system terminal (cmd, PowerShell, bash, zsh, etc.).

```bash
python maze_runner.py
```

## 🎨 Example Output

When you run the script, the maze will be shown and the path exploration will animate step by step until the end is reached.
```
* * * * * O * * *
*               *
*   * *   * *   *
*   *       *   *
*   *   *   *   *
*   *   *   * * *
*               *
* * * * * * * X *
```
- As the program runs, you’ll see red X marks showing the BFS path exploration until the goal is found.
- You can change the shape of the maze by editing the maze list in the code.

## 🔧 Requirements
- Python 3.x
- Standard library modules only:
- curses library
- queue
- - time
- No external dependencies are required.

## 📌 Notes
- Press any key after the maze finishes solving to exit.
- If you want it to run inside VS Code, you’ll need to adapt it to use print animations or matplotlib instead of curses.







