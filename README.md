# 💾 Automated File Backup Script
This Python script automatically creates a daily backup of a folder by copying it into a destination directory. Each backup is stored in a subfolder named with the current date.

## ✨ Features
- Automatically copies files from a source folder to a backup folder
- Creates a new subfolder named after today’s date (YYYY-MM-DD)
- Runs every day at a scheduled time using the schedule module
- Can overwrite/update backups if needed (Python 3.8+)

## ⚡ Requirements
- Python 3.8 or later

## 📦 Install required library:
```
pip install schedule
```
- A Backup folder must already exist at the destination path you set in:
```
destination_dir = "C:/Users/HP/OneDrive/Desktop/Backup"
```

## 🚀 Usage
- Clone or download this script.
- Update the following paths in the script:
```
source_dir = "C:/Users/HP/OneDrive/Desktop/Wallpapers"
destination_dir = "C:/Users/HP/OneDrive/Desktop/Backup"
```
- Make sure the Backup folder already exists at the destination path.
- Run the script:
```
python automated_backup.py
```
- The script will run continuously and perform the backup every day at 18:55.

⚙️##  Customization

🕒 Change schedule time:
```
schedule.every().day.at("18:55").do(lambda: copy_folder_to_directory(source_dir, destination_dir))
```
- Overwrite existing backups (default with dirs_exist_ok=True).

📂 Keep separate backups per day (e.g., Backup/2025-09-25).

📂 Example Output

If today is 2025-09-25, after running the script your backup directory will look like:

Backup/
 ├── 2025-09-24/
 ├── 2025-09-25/

💡 Notes

🖥️ To make it run automatically without keeping the terminal open:

⚙️ Use Windows Task Scheduler (recommended).

📦 Or convert to .exe with PyInstaller

.







