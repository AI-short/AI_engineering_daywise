# Day 2: Variables, Data Types, Input/Output, Type Casting

# 1. Variables
x = 10
y = "Hello"
z = 3.14

# 2. Data Types
a = 10
b = 4.5
c = "Python"
d = True

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'str'>
print(type(d))  # Output: <class 'bool'>

# 3. Taking User Input
name = input("Enter your name: ")
print("Hello,", name)

# 4. Type Casting (Converting types)
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print("Age:", age)
print("Height:", height)

# 5. Practice Examples

# Example 1: Ask user for favorite food and print
food = input("Enter your favorite food: ")
print("You like", food)

# Example 2: Ask for two numbers and print their sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# Example 3: Convert float input to int and print
f = float(input("Enter a decimal number: "))
print("As integer:", int(f))
