# Create a function that determines whether or not it's possible to split a pie fairly given these three parameters:
# Example:
# equal_slices(11, 5, 2) ➞ True
# 5 people x 2 slices each = 10 slices < 11 slices 
# equal_slices(11, 5, 3) ➞ False
# 5 people x 3 slices each = 15 slices > 11 slices

def equal_slices(total, people, each):
	if people * each <= total:
		return True
	else:
		return False
print(equal_slices(11, 5, 2))
print(equal_slices(11, 5, 3))