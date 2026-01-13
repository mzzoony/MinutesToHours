# MinutesToHours
A lightweight Windows desktop app built with (Python + Tkinter) that converts minutes into decimal hours (e.g., `37 → 0.62`) handy for quick time entry and timesheets.

# Screenshot
<img width="383" height="246" alt="App Screenshot" src="https://github.com/user-attachments/assets/a95fe6db-2353-492f-b89a-1e14ca5c3619" />



## Features
- Convert minutes → hours instantly
- Clean, simple UI
- Works on Windows
- Downloadable Windows (.exe) via GitHub (Releases)

# Download (Windows)
1. Go to the (Releases) section of this repository.
2. Download (MinutesToHours.exe)
3. Run it (Windows may show a security prompt for unsigned apps).

# Run Locally (Developer)
From the project root:
python src/app.py

#Build a Windows .exe (PyInstaller)
1) Install PyInstaller
   py -m PyInstaller --onefile --windowed --name MinutesToHours src/app.py
2) Build
   py -m PyInstaller --onefile --windowed --name MinutesToHours src/app.py
3) Output
   dist/MinutesToHours.exe
   
#Project Structure
MinutesToHours/
├─ src/
│  └─ app.py
├─ assets/
│  ├─ icon.ico
│  └─ screenshot.png
├─ README.md
├─ LICENSE
└─ .gitignore

#License
::contentReference[oaicite:0]{index=0}

