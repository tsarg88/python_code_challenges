# Write a function that takes the last number of a consecutive list of numbers and returns the total of all numbers up to and including it.
# Example:
# add_up_to(3) ➞ 6
# # 1 + 2 + 3 = 6
# add_up_to(10) ➞ 55
# # 1 + 2 + 3 + ... + 10 = 55
# add_up_to(7) ➞ 28
# # 1 + 2 + 3 + ... + 7 = 28

def add_up_to(n):
	return sum(range(0, n + 1))
print(add_up_to(3))
print(add_up_to(10))
print(add_up_to(7))

