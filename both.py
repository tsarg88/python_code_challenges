# Write a function that checks if two numbers are:
# Smaller than 0
# Greater than 0
# Exactly 0
# Example:
# both(6, 2) ➞ True
# both(0, 0) ➞ True
# both(-1, 2) ➞ False
# both(0, 2) ➞ False

# Method 1
def both(n1, n2):
    return n1 == n2 or n1 * n2 > 0
# print(both(-2, -3))

# Method 2
def both(n1, n2):
    return (n1 > 0 and n2 > 0) or (n1 == 0 and n2 == 0) or (n1 < 0 and n2 < 0)
print(both(6, 2))
print(both(0, 0))
print(both(-1, 2))
print(both(0, 2))
