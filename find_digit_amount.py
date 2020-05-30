# Create a function that takes a number as an argument and returns the amount of digits it has
# Example:
# find_digit_amount(123) ➞ 3
# find_digit_amount(56) ➞ 2

def find_digit_amount(num):
	return len(str(num))
print(find_digit_amount(123))
print(find_digit_amount(56))
