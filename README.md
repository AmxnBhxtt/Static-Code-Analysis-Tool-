# Git Repository Cloner and Code Analysis Script

Author: Aman Bhatt
Date: January 24

## Description

This script allows you to clone a Git repository from a specified URL and perform static code analysis using Flake8 on the cloned files. It is designed to help developers quickly assess the code quality of a remote repository by analyzing its Python files.

## Usage

1. Ensure that you have the 'git' command-line tool and Python 3.10 installed on your system.
2. Run this script using Python 3.10 or a later version.

## Dependencies

- git (command-line tool)
- Python 3.10
- Flake8 (Python linting tool)

## Modules Used

- git: Provides functionality to interact with Git repositories.
- os: Allows interaction with the operating system, file paths, and directories.
- subprocess: Enables running shell commands from Python.

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using the following command: `python script_name.py` (replace `script_name.py` with the actual script filename).

## Example Output

After running the script, you will see output indicating whether the repository was successfully cloned and the relative paths of the files in the cloned repository. Additionally, the script will perform static code analysis using Flake8 and display the analysis output for each file.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize and expand this README to include any additional information relevant to your project or repository.
