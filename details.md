# Millionaire Game Project

## Purpose
This project is a command-line quiz game inspired by the popular Indian TV show "Kaun Banega Crorepati" (KBC). The game presents users with 10 multiple-choice questions across various fields like history, science, geography, and more. Players must select the correct answer from four options (A, B, C, D). Correct answers advance the player to the next question and potentially unlock prize money, while incorrect answers end the game with the last secured amount. The game includes safe havens at certain milestones to ensure players don't lose all progress.

## Concepts Used
- **Data Structures**: The questions are stored in a list of dictionaries, where each dictionary contains the question text, a list of options, and the correct answer. This allows for easy access and iteration.
- **Control Flow**: A `for` loop iterates through the questions. `if-else` statements check user answers and handle game logic, including prize awarding and game termination.
- **Input/Output Operations**: `print()` is used to display questions and feedback, while `input()` captures user responses.
- **String Manipulation**: F-strings (formatted string literals) are used for dynamic output, such as displaying questions and prizes.
- **Arithmetic Operations**: The modulo operator (`%`) is used to cycle through prize amounts safely, ensuring index bounds are respected.
- **Error Handling**: Basic validation ensures the game handles user input gracefully, though advanced error checking could be added.

## Basic Requirements
- **Python Version**: Python 3.x (tested with Python 3.14, but should work with 3.6+).
- **No External Dependencies**: The program uses only built-in Python modules, so no additional packages need to be installed.
- **Execution Environment**: Run the script (`main.py`) in a terminal or command prompt. Ensure the terminal supports interactive input (e.g., PowerShell on Windows).
- **System Requirements**: Any modern operating system (Windows, macOS, Linux) with Python installed. Minimal hardware requirements as it's a text-based application.