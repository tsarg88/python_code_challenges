# Write a function that takes an integer and:
#  If the number is a multiple of 3, return "Hello".
#  If the number is a multiple of 5, return "World".
#  If the number is a multiple of both 3 and 5, return "Hello World".
# Explanation:
# hello_world(3) ➞ "Hello"
# hello_world(5) ➞ "World"
# hello_world(15) ➞ "Hello World"

def hello_world(num):
    return 'Hello World' if num % 3 == 0 and num % 5 == 0 else 'Hello' if num % 3 == 0 else 'World' if num % 5 == 0 else ''
print(hello_world(3))
print(hello_world(5))
print(hello_world(15))
print(hello_world(1))
