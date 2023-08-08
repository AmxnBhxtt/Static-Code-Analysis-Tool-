import git
import os
import subprocess

# Define the URL of the Git repository you want to clone
repo_url = 'https://github.com/geekcomputers/Python.git'

# Get the path to your desktop
desktop_path = os.path.expanduser('~/Desktop')

# Define the local path where you want to store the cloned repository on your desktop
local_path = os.path.join(desktop_path, 'repository')

try:
    # Clone the repository
    git.Repo.clone_from(repo_url, local_path)
    print('Repository cloned successfully!')
except git.exc.GitCommandError as e:
    if 'destination path' in str(e):
        print('Repository already exists. Parsing through existing files...')

# Iterate over the files in the cloned repository
for root, dirs, files in os.walk(local_path):
    for file in files:
        file_path = os.path.join(root, file)

        # Get the relative path of the file
        relative_path = os.path.relpath(file_path, local_path)

        # Perform your desired operations on the file
        # For example, print the relative path
        print(relative_path)

        try:
            # Perform static code analysis using Flake8
            flake8_output = subprocess.check_output(['/Library/Frameworks/Python.framework/Versions/3.10/bin/python3', '-m', 'flake8', file_path], stderr=subprocess.STDOUT).decode('utf-8')
            print(flake8_output)
        except subprocess.CalledProcessError as e:
            # Handle the non-zero exit status error
            print(f"Error analyzing file: {file_path}")
            print(f"Error message: {e.output.decode('utf-8')}")
