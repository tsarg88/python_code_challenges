# Given a list of numbers, negate all elements contained within.
# Example:
# negate([1, 2, 3, 4]) ➞ [-1, -2, -3, -4]
# negate([-1, 2, -3, 4]) ➞ [1, -2, 3, -4]

def negate(lst):
	return [-n for n in lst]
print(negate([1, 2, 3, 4]))
print(negate([-1, 2, -3, 4]))
