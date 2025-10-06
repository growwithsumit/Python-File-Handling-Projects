# Python File Handling Projects

This repository contains two simple Python scripts that demonstrate fundamental file input/output (I/O) operations. These projects cover writing to a file, appending data, reading from a file, and handling common errors.

## 📂 Projects Included

1.  **Read a File and Handle Errors**: A script that safely reads a text file and handles the case where the file might not exist.
2.  **Write and Append Data to a File**: An interactive script that writes and appends user-provided text to a file.

---

## Project 1: Read a File and Handle Errors

This script (`Read a File and Handle Errors.py`) demonstrates how to open and read a text file while gracefully handling the `FileNotFoundError`.

### ✨ Features
* Opens and reads a file named `sample.txt`.
* Prints the file's content to the console.
* Provides a clean error message if `sample.txt` is not found, preventing the program from crashing.

#### Expected Output

**If `sample.txt` exists:**

Reading file content:

Line 1: This is a sample text file.

Line 2: It contains multiple lines.


**If `sample.txt` does not exist:**

Error: The file 'sample.txt' was not found.


## Project 2: Write and Append Data to a File

This interactive script (`Write and Append Data to a File.py`) demonstrates how to write new content to a file (overwriting existing data) and how to append new data to the end of that file.

### ✨ Features
* Prompts the user to enter text, which is written to `output.txt`. This **overwrites** any previous content.
* Prompts the user for additional text to **append** to a new line in `output.txt`.
* Reads the entire file and displays the final content to the user.


#### Example Usage

Here is a sample of what you'll see when you run the script:

Enter text to write to the file: Hello, Python!

Data successfully written to output.txt

Enter additional text to append: Learning file handling in python.

Data successfully append.

Final content of output.txt:

Hello, Python!

Learning file handling in python.
