🎥 YouTube Video Downloader (Tkinter + Pytube)

This is a simple Python application that lets you download YouTube videos in the highest available resolution.
It uses pytube
 for fetching and downloading videos and Tkinter for folder selection.

✨ Features

📌 Download YouTube videos in highest available resolution (MP4).

📌 GUI folder picker for choosing download directory.

📌 Lightweight and easy to use.

🚀 Requirements

Make sure you have the following installed:

Python 3.8+

Required Python packages:

pip install pytube tkinter


⚠️ Note: tkinter usually comes pre-installed with Python. If not, you can install it separately depending on your OS.

📂 How to Run

Clone or download this project.

Open a terminal in the project folder.

Run the script:

python main.py


Enter a valid YouTube video URL when prompted.

A dialog box will open → select the folder where you want to save the video.

The video will start downloading.

🖼 Example Output
Enter a YouTube url: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Selected folder: C:/Users/HP/Videos
Download initialized...
Video downloaded successfully!


If no folder is selected:

Enter a YouTube url: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Selected folder: 
Invalid save location.

🛠 Troubleshooting

If you get RegexMatchError or HTTP Error 400, update pytube:

pip install --upgrade pytube


Make sure the YouTube URL is public and accessible.