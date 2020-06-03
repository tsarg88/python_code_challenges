# Create a function that searches for the index of a given item in a list. If the item is present, it should return the index, otherwise, it should return -1.
# Example:
# search([1, 2, 3, 4], 3) ➞ 2
# search([2, 4, 6, 8, 10], 8) ➞ 3
# search([1, 3, 5, 7, 9], 11) ➞ -1

def search(lst, item):
	return lst.index(item) if item in lst else -1
print(search([1, 2, 3, 4], 3))
print(search([2, 4, 6, 8, 10], 8))
print(search([1, 3, 5, 7, 9], 11))
	