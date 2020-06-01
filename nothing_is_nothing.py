# Given any number of parameters (which is signified using *args syntax), return True if none of the variables are falsy/empty.
# Example:
# nothing_is_nothing(0, False, [], {}) ➞ False
# nothing_is_nothing(33, "Hello", (True, True, 3)) ➞ True
# nothing_is_nothing(True, None) ➞ False

def nothing_is_nothing(*args):
	return all(args)
print(nothing_is_nothing(0, False, [], {}))
print(nothing_is_nothing(33, "Hello", (True, True, 3)))
print(nothing_is_nothing(True, None))
