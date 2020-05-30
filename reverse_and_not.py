# Write a function that takes an integer i and returns an integer with the integer backwards followed by the original integer.
# Example:
# reverse_and_not(123) ➞ 321123
# reverse_and_not(152) ➞ 251152

def reverse_and_not(i):
	return int(str(i)[::-1] + str(i))
print(reverse_and_not(123))
print(reverse_and_not(152))
