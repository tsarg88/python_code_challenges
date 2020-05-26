# Write a function to check if a list contains a particular number.
# Example:
# check([1, 2, 3, 4, 5], 3) ➞ True
# check([1, 1, 2, 1, 1], 3) ➞ False

def check(lst, el):
	return el in lst

print(check([1, 2, 3, 4, 5], 3))
print(check([1, 2, 3, 4, 5], 8))