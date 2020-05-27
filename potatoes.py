# Create a function to return the amount of potatoes there are in a string.
# Example:
# potatoes("potato") ➞ 1
# potatoes("potatopotato") ➞ 2

def potatoes(potato):
	return potato.count('potato')
print(potatoes("potato"))
print(potatoes("potatopotato"))