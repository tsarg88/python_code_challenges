# Write a function that takes two numbers and returns if they should be added, subtracted, multiplied or divided to get 24. If none of the operations can give 24, return None.
# Example:
# operation(15, 9) ➞ "added"
# operation(26, 2) ➞ "subtracted"
# operation(11, 11) ➞ None
# Notes:
# Only integers are used as test input.
# Numbers should be added, subtracted, divided or multiplied in the order they appear in the parameters.
# The function should return either "added", "subtracted", "divided", "multiplied" or None.

def operation(num1, num2):
    if num1 + num2 == 24:
        return 'added'
    if num1 - num2 == 24:
        return 'subtracted'
    if num1 * num2 == 24:
        return 'multiplied'
    if num1 / num2 == 24:
        return 'divided'
print(operation(15, 9))
print(operation(26, 2))
print(operation(11, 11))

# Method 2
# def operation(a, b):
# 	return {a+b: "added", a-b: "subtracted", a*b: "multiplied", a/b: "divided"}.get(24)
# print(operation(15, 99))
