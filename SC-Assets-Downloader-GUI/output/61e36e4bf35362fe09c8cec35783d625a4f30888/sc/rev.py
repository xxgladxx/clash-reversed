import os
import shutil
import subprocess

def process_file(file_path):
    if file_path.endswith('_tex.sc'):
        command = ['python', 'dumpsc.py', file_path]
        return

    subprocess.run(command)

def clone_directory_structure(source_dir, dest_dir):
    for root, dirs, files in os.walk(source_dir):
        # Create corresponding directories in the destination directory
        for directory in dirs:
            source_path = os.path.join(root, directory)
            dest_path = os.path.join(dest_dir, os.path.relpath(source_path, source_dir))
            os.makedirs(dest_path, exist_ok=True)

        # Process files in the current directory
        for file in files:
            source_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_dir, os.path.relpath(source_file_path, source_dir))
            shutil.copyfile(source_file_path, dest_file_path)
            process_file(dest_file_path)

if __name__ == "__main__":
    source_directory = R""

    clone_directory_structure(source_directory)