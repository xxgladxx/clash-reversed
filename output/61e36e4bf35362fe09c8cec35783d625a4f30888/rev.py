import os
import subprocess

def find_files(directory, pattern):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(pattern):
                found_files.append(os.path.join(root, file))
    return found_files

def main():
    # Find all files ending with '_tex.sc' recursively in the current directory
    files = find_files('.', '_tex.sc')

    # Loop through each found file
    for file_path in files:
        # Execute the dumpsc.py script with the file path as an argument using subprocess
        subprocess.run(['python', './dumpsc.py', file_path])

if __name__ == "__main__":
    main()
