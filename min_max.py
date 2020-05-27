# Create a function that accepts a list of numbers and return both the minimum and maximum numbers, in that order (as a list).
# Example:
# min_max([1, 2, 3, 4, 5]) ➞ [1, 5]
# min_max([2334454, 5]) ➞ [5, 2334454]

def min_max(nums):
	return [min(nums), max(nums)]
print(min_max([1, 2, 3, 4, 5]))
print(min_max([2334454, 5]))