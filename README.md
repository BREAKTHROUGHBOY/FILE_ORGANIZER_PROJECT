# FILE_ORGANIZER_PROJECT ->> Smart File Sorting Tool

This project automatically organizes files (images, documents, videos, and audio) into categorized folders using Python.  
It’s a practical project that demonstrates file handling, JSON configuration, and modular Python structure.

---

## 🚀 Features
- Automatically detects and sorts files based on extensions.
- JSON-based configuration for flexible file type categories.
- Built with clean modular design (`main.py`, `fileutils.py`).
- Error handling for missing directories and configs.
- Beginner-friendly and real-world applicable.

---

## 🏗️ Project Structure


FileOrganizerProject/
│
├── main.py # Entry point of the program
├── fileutils.py # Utility functions (organize, load config, etc.)
├── config.json # File type configuration
├── test_files/ # Test directory with sample files
└── README.md # Documentation


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/FileOrganizerProject.git
cd FileOrganizerProject

2️⃣ Run the Script
python main.py


Make sure you have a test_files/ folder in the same directory with files you want to organize.

🧩 Example Config (config.json)
{
  "file_types": {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"]
  }
}

🧠 Concepts Used

File I/O (os, shutil)

JSON parsing (json)

Path management (os.path)

Modular architecture (import, reusable functions)

Exception handling

👤 Author

Player 1 (Trillionare)
🚀 Aiming to build advanced, practical AI systems — one project at a time.
💡 GitHub: @BREAKTHROUGHBOY

🪄 License

MIT License © 2025 Player 1


---

## 💻 STEP 4 — Pushing It to GitHub (The Exact Commands)

Open terminal (inside your project folder):

```bash
cd path/to/FileOrganizerProject
git init
git add .
git commit -m "Initial commit: File Organizer project"


Then, create a new repository on GitHub manually (call it FileOrganizerProject).

Copy the link it gives (like):

https://github.com/BREAKTHROUGHBOY/FileOrganizerProject.git


Now link it to your local repo:

git remote add origin https://github.com/your-username/FileOrganizerProject.git
git branch -M main
git push -u origin main


Done ✅ — your project is now live on GitHub.

Thank You !
