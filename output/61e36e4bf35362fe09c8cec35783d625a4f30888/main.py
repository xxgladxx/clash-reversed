import os
import subprocess

def main():
    # Get the current directory
    current_dir = os.getcwd()

    # Walk through the directory tree
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            # Check if the file ends with '.sc' and does not end with '_tex.sc'
            if file.endswith('.sc') and not file.endswith('_tex.sc'):
                # Execute quickbms command for each matching file
                file_path = os.path.join(root, file)
                subprocess.run([R"C:\Users\aksha\Desktop\quickbms\quickbms.exe", './clash_royale.bms', file_path])

if __name__ == "__main__":
    main()
