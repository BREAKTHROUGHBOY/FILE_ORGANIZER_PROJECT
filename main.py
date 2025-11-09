# main.py
from file_utils import organize_files

def main():
    print("=== File Organizer Project ===\n")
    folder = input("Enter folder path to organize (or press Enter for 'testfiles'): ").strip()
    if not folder:
        folder = "test_files"

    print("\n🔄 Organizing files...")
    organize_files(folder)
    print("\n✅ Done! All files organized successfully.")

if __name__ == "__main__":
    main()

print("Mission Successful !")