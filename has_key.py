# Write a function that returns True if a dictionary contains the specified key, and False otherwise.
# Example:
# has_key({ "a": 44, "b": 45, "c": 46 }, "d") ➞ False
# has_key({ "craves": True, "midnight": True, "snack": True }, "midnight") ➞ True

def has_key(dictionary, key):
	if key in dictionary:
		return True
	else:
		return False
print(has_key({ "a": 44, "b": 45, "c": 46 }, "d"))
print(has_key({ "craves": True, "midnight": True, "snack": True }, "midnight"))