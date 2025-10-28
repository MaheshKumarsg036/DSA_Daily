# Array Questions (If-Else Focused)
# 1. Positive or Negative
# Problem: Given a number, check if it is positive, negative, or zero.
# Example: Input: -5 → Output: Negative

def check_number(num):
    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else:
        print("zero")


# 2. Even or Odd
# Problem: Check if a number is even or odd using if-else.
# Example: Input: 7 → Output: Odd

def check_even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


# 3. Compare Two Numbers
# Problem: Take two numbers as input and print which one is greater, or if they
# are equal.
# Example: Input: 4, 4 → Output: Equal
def greater_number(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)