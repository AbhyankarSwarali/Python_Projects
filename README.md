# Python Alarm Clock ⏰
A simple Python-based alarm clock that waits for a given time and then plays an alarm sound. It shows a live countdown timer in the terminal and plays a sound when the time is up.

---

## Features
- Countdown display in `MM:SS` format.
- Works with custom minute/second input.
- Plays an alarm sound when the timer ends.
- Supports both CMD and VS Code terminal.

---

## Requirements
- Python 3.8 or above  
- Dependencies:
  ```
  bash
  pip install playsound3
  ```
- or (recommended for VS Code):
```
bash
Copy code
pip install simpleaudio
```

## Usage
- Clone or download this script.
- Place an audio file (alarm.mp3 or alarm.wav) in the same directory as the script.
- Run the script:
```
bash
Copy code
python alarm.py
```
- Enter the time you want to wait:
```
bash
Copy code
How many minutes to wait? 0
How many seconds to wait? 10
```
- The countdown will appear, and the alarm will play when the time is up.

## Troubleshooting
- Alarm sound doesn’t play in VS Code
- playsound3 may fail inside the VS Code integrated terminal.
- **Fix:** Either run the script in **Command Prompt** or **PowerShell** or install **simpleaudio**:
```
bash
Copy code
pip install playsound3
```
- Then replace the sound-playing part in your code:
```
python
Copy code
from playsound3 import playsound

def play_alarm():
    wave_obj = sa.WaveObject.from_wave_file("alarm.wav")  # use WAV instead of MP3
    play_obj = wave_obj.play()
    play_obj.wait_done()
```
❌ Countdown doesn’t update properly in VS Code
Add flush=True to the print statement:

python
Copy code
print(f'{CLEAR_AND_RETURN}Alarm will ring in {minutes_left:02d}:{seconds_left:02d}', flush=True)
Example Run
bash
Copy code
How many minutes to wait? 0
How many seconds to wait? 5

Alarm will ring in 00:04
Alarm will ring in 00:03
Alarm will ring in 00:02
Alarm will ring in 00:01
Alarm will ring in 00:00

🔔 Alarm ringing! 🔔






