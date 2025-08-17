# 🧮 Math Quiz Game (Python)

This is a simple command-line **Math Quiz** built in Python.\
It generates random math problems and tracks how quickly you can solve
them.

------------------------------------------------------------------------

## 📌 Features

-   Random math problems using `+`, `-`, `*`\
-   User-defined number of problems (configurable in the code)\
-   Tracks mistakes made and total completion time\
-   Simple and interactive console interface

------------------------------------------------------------------------

## 🚀 How to Use

1.  Clone this repository or copy the script.\

2.  Run the Python file:

    ``` bash
    python math_quiz.py
    ```

3.  Press Enter to start solving problems.\

4.  Answer each math problem until all are solved.

------------------------------------------------------------------------

## 📝 Example Run

``` bash
Press enter to start
------------
Problem 1: 7 * 5 = 35
Problem 2: 9 - 6 = 3
Problem 3: 10 + 11 = 21
...
------------
Great work!
You finished in 14 seconds!
```

------------------------------------------------------------------------

## 📷 Code Snapshot

Here's the core **problem generator** function from the project:

``` python
def generate_prob():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)
    return expr, answer
```

------------------------------------------------------------------------

✅ That's it! Run the script and test your math skills.
