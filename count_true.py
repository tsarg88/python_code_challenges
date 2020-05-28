# Create a function which returns the number of True values in a list.
# Example:
# count_true([True, False, False, True, False]) ➞ 2
# count_true([False, False, False, False]) ➞ 0

def count_true(lst):
	return lst.count(True)
print(count_true([True, False, False, True, False]))
print(count_true([False, False, False, False]))
