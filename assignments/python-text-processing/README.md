# 📘 Assignment: Python Text Processing

## 🎯 Objective

Learn to manipulate text data using Python, including reading from files, processing strings, and writing results back to files. This assignment will help you understand basic text processing techniques essential for data analysis and file handling.

## 📝 Tasks

### 🛠️ Task 1: Read and Count Words

#### Description
Write a program that reads a text file and counts the total number of words in it.

#### Requirements
Completed program should:

- Read from a file named 'input.txt' (you can create this file with some sample text)
- Count words by splitting on spaces
- Print the total word count to the console
- Handle basic error cases (e.g., file not found)

### 🛠️ Task 2: Text Cleaning Function

#### Description
Create a function that processes a string to remove punctuation and convert it to lowercase.

#### Requirements
Completed program should:

- Define a function called `clean_text(text)`
- Remove all punctuation marks (!, ., ,, ?, etc.)
- Convert the text to lowercase
- Return the cleaned string
- Test the function with sample strings

### 🛠️ Task 3: Process and Save Text

#### Description
Combine the previous tasks to read text from a file, clean it, and write the processed text to a new file.

#### Requirements
Completed program should:

- Read each line from 'input.txt'
- Apply the cleaning function to each line
- Write the cleaned lines to 'output.txt'
- Print a success message when done
- Handle file operations properly (open/close files)