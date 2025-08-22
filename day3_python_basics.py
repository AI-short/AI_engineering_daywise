# Day 3: Strings in Python with complete explanations

# Define a string variable 'word' with value "Python"
word = "Python"

# Print the first character of the string (index 0)
print(word)  # Output: P

# Print the last character using negative indexing (-1)
print(word[-1])  # Output: n

# Slice from index 0 to 3 (3 not included) -> returns substring from 0 to 2
print(word[0:3])  # Output: Pyt

# Slice from beginning to index 4 (4 not included)
print(word[:4])  # Output: Pyth

# Slice from index 2 to the end of the string
print(word[2:])  # Output: thon

# Print the entire string (equivalent to [:])
print(word[:])  # Output: Python

# Define a string with leading and trailing whitespace
course = "  Python Programming  "

# Remove whitespace from the both ends
print(course.strip())  # Output: Python Programming

# Convert all letters to uppercase
print(course.upper())  # Output:   PYTHON PROGRAMMING  

# Replace "Python" with "Java"
print(course.replace("Python", "Java"))  # Output:   Java Programming  

# Find the starting position of substring "Prog"
print(course.find("Prog"))  # Output: 7

# Count how many times 'm' appears in the string
print(course.count("m"))  # Output: 2

# Split the string into a list of words by whitespace
print(course.split())  # Output: ['Python', 'Programming']

# Concatenate strings using '+'
greeting = "Hello" + " " + "World"
print(greeting)  # Output: Hello World

# Repeat string multiple times using '*'
print("Ha" * 3)  # Output: HaHaHa

# Escape single quote inside single quoted string using backslash
print('I\'m learning Python')  # Output: I'm learning Python

# New line character causes text to be on the next line
print("Hello\nWorld")  
# Output:
# Hello
# World

# Tab character adds a horizontal tab space
print("Column 1\tColumn 2")  
# Output: Column 1   Column 2

# Using formatted string (f-string) for interpolation
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  
# Output: My name is Alice and I am 30 years old.
