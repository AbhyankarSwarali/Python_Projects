🏞️ Adventure Game

This is a simple text-based adventure game written in Python.  
The game allows the player to make choices at different stages, leading to different outcomes — either winning, losing, or running into unexpected scenarios.  

---

🎮 How to Play

1. Run the Python script.
2. Enter your name when prompted.
3. Make choices by typing the options shown (e.g., left, right, swim, walk, cross, back, yes, no).
4. The game ends when you either win or lose depending on your choices.

---

🧭 Game Flow

- You start on a dirt road with two paths:  
  - Left → Leads to a river (options: walk / swim)  
    - swim → You get eaten by an alligator. (Lose)  
    - walk → You run out of water. (Lose)  

  - Right → Leads to an old bridge (options: cross / back)  
    - back → You return to the main road. (Lose)  
    - cross → You meet a stranger (options: yes / no)  
      - yes → The stranger gives you the secret to becoming the richest person. (Win 🎉)  
      - no → You ignore him, and he kills you. (Lose)  

---

⚙️ Requirements

- Python 3.x installed on your system

---

▶️ How to Run

python adventure_game.py

---

📌 Example Run

Enter your name: Alex  
Welcome Alex to this adventure game!  
You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? right  
You reached an old bridge. It looks wobbly. Do you want to cross it or head back (cross/back)? cross  
You crossed the bridge and met a stranger. Do you want to talk to him (yes/no)? yes  
The stranger told you the secret for being the richest person  
You win  
Hope you enjoyed the game Alex  

---

🚀 Future Enhancements
- Add more paths and scenarios  
- Implement a scoring system  
- Allow saving progress  

---

👤 Author: Your Name  
📅 Version: 1.0  
