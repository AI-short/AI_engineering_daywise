# ========================================
# DAY 4 – OPERATORS IN PYTHON
# ========================================

# -------------------------------
# 1. Arithmetic Operators
# -------------------------------
a = 10
b = 3

print("Addition:", a + b)        # 10 + 3 = 13
print("Subtraction:", a - b)     # 10 - 3 = 7
print("Multiplication:", a * b)  # 10 * 3 = 30
print("Division:", a / b)        # 10 / 3 = 3.333...
print("Floor Division:", a // b) # 10 // 3 = 3
print("Modulus:", a % b)         # 10 % 3 = 1
print("Exponent:", a ** b)       # 10 ** 3 = 1000

# Output:
# Addition: 13
# Subtraction: 7
# Multiplication: 30
# Division: 3.3333333333333335
# Floor Division: 3
# Modulus: 1
# Exponent: 1000

# -------------------------------
# 2. Comparison (Relational) Operators
# -------------------------------
x = 5
y = 10

print(x == y)   # False → 5 is not equal to 10
print(x != y)   # True  → 5 is not equal to 10
print(x > y)    # False → 5 is not greater than 10
print(x < y)    # True  → 5 is less than 10
print(x >= 5)   # True  → 5 is equal to 5
print(y <= 5)   # False → 10 is not ≤ 5

# Output:
# False
# True
# False
# True
# True
# False

# -------------------------------
# 3. Logical Operators
# -------------------------------
a = True
b = False

print(a and b)  # False → both must be True
print(a or b)   # True  → at least one is True
print(not a)    # False → reverse of True

# Output:
# False
# True
# False

# Example with numbers
age = 20
print(age > 18 and age < 25)  # True → 20 is between 18 and 25
print(age > 25 or age == 20)  # True → second condition is True

# Output:
# True
# True

# -------------------------------
# 4. Bitwise Operators
# -------------------------------
x = 6   # binary: 110
y = 3   # binary: 011

print("AND:", x & y)        # 110 & 011 = 010 → 2
print("OR:", x | y)         # 110 | 011 = 111 → 7
print("XOR:", x ^ y)        # 110 ^ 011 = 101 → 5
print("NOT:", ~x)           # ~110 → -(6+1) = -7
print("Left Shift:", x << 1) # 110 → 1100 → 12
print("Right Shift:", x >> 1)# 110 → 11 → 3

# Output:
# AND: 2
# OR: 7
# XOR: 5
# NOT: -7
# Left Shift: 12
# Right Shift: 3

# -------------------------------
# 5. Operator Precedence
# -------------------------------
result = 2 + 3 * 4
print(result)   # 2 + (3*4) = 14

result = (2 + 3) * 4
print(result)   # (5) * 4 = 20

result = 2 * 3 ** 2
print(result)   # 2 * (9) = 18

# Output:
# 14
# 20
# 18
