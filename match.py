# Write a function that validates whether two strings are identical. Make it case insensitive.
# Example:
# match("hello", "hELLo") ➞ True
# match("motive", "emotive") ➞ False

def match(s1, s2):
	if s1.casefold() == s2.casefold():
		return True
	else:
		return False
print(match("hello", "hELLo"))
print(match("motive", "emotive"))