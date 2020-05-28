# Create a function that returns True if the first list can be nested inside the second.
# list1 can be nested inside list2 if:
#     1. list1's min is greater than list2's min.
#     2. list1's max is less than list2's max.
# Example:
# can_nest([3, 1], [4, 0]) ➞ True
# can_nest([9, 9, 8], [8, 9]) ➞ False

def can_nest(list1, list2):
	return min(list1) > min(list2) and max(list1) < max(list2)
print(can_nest([3, 1], [4, 0]))
print(can_nest([9, 9, 8], [8, 9]))