# fileutils.py
import os
import shutil
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

def load_config():
    """Load configuration safely."""
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"❌ Config file not found at: {CONFIG_PATH}")

    with open(CONFIG_PATH, "r") as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("⚠️ Invalid JSON format in config.json. Please fix it.")

    return config
print(load_config())

def organize_files(folder_path):
    """Organize files into folders based on extensions."""
    config = load_config()
    file_types = config.get("file_types", {})

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue  # skip folders

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Match extension
        moved = False
        for folder_name, extensions in file_types.items():
            if ext in extensions:
                move_file(file_path, folder_path, folder_name)
                moved = True
                break

        if not moved:
            move_file(file_path, folder_path, "Others")


def move_file(src_path, base_path, folder_name):
    """Move file to a categorized folder."""
    dest_folder = os.path.join(base_path, folder_name)
    os.makedirs(dest_folder, exist_ok=True)
    shutil.move(src_path, dest_folder)
    print(f"✅ Moved: {os.path.basename(src_path)} → {folder_name}/")
