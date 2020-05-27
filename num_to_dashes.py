# Create a function that takes a number (from 1 - 60) and returns a corresponding string of hyphens.
# Example:
# num_to_dashes(1) ➞ "-"
# num_to_dashes(5) ➞ "-----"

# Method 1:
def num_to_dashes(num):
	dashes = ''
	counter = 0
	while counter < num:
		dashes += '-'
		counter += 1
	return dashes
print(num_to_dashes(1))
print(num_to_dashes(3))

# Method 2
def num_to_dashes(num):
	return "-" * num
print(num_to_dashes(1))
print(num_to_dashes(3))