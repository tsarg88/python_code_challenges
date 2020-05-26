# Create a function that returns True if two lists contain identical values, and False otherwise.
# Example:
# check_equals([1, 2], [1, 3]) ➞ False
# check_equals([1, 2], [1, 2]) ➞ True

def check_equals(lst1, lst2):
	lst1.sort()
	lst2.sort()
	if lst1 == lst2:
		return True
	else:
		return False
print(check_equals([1, 2], [1, 3]))
print(check_equals([1, 2], [1, 2]))