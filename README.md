# Horror Slashers Dictionary 🎃🔪
An interactive command-line Python script created for Halloween. The user inputs a famous horror movie, and the program reveals the corresponding slasher (killer). 

## Features
* **Case and space insensitive:** Automatically handles messy user inputs (extra spaces, uppercase/lowercase) using string manipulation methods.
* **Dynamic catalog:** The list of available movies is automatically generated from the dictionary keys.
* **Interactive loop:** The program allows the user to search for multiple movies without restarting.
* **Input validation:** Ensures the user provides valid responses to continue or finish.

## Python Concepts Used
As a learning project, this script covers several fundamental Python concepts:
* **Dictionaries:** For the database of movies and killers.
* **List Comprehensions:** Used to format the movie catalog dynamically.
* **String Methods:** `.split()`, `.join()`, `.lower()`, `.title()`, `.strip()`.
* **Control Flow:** `while` loops (with an inner validation loop), `if/else` statements, and ternary operators.
* **Membership Operators:** `in` to check if a movie exists in the database.

## How to Run
1. Make sure you have Python installed.
2. Clone this repository or download the `slashers_dictionary.py` file.
3. Open your terminal and run:
   `python slashers_dictionary.py`

---
*Created by At0mic-Samurai as a Python learning milestone.*
