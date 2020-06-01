# Given a fraction as a string, return whether or not it is greater than 1 when evaluated.
# Example:
# greater_than_one("1/2") ➞ False
# greater_than_one("7/4") ➞ True
# greater_than_one("10/10") ➞ False

def greater_than_one(frac):
	return eval(frac) > 1
print(greater_than_one("1/2"))
print(greater_than_one("7/4"))
print(greater_than_one("10/10"))
