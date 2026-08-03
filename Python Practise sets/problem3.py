import os

def print_directory_contents(path='.'):
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
#  You can now type this and nobody will see it

    directory_path = input("Enter directory path (enter for current directory): ").strip() or '.'
    print_directory_contents(directory_path)
