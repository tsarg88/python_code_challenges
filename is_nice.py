# The ternary operator (sometimes called Conditional Expressions) in python is an alternative to the if... else... statement.
# It is written in the format:
    # condition_if_true if condition else condition_if_false
# Example:
# is_nice = True

# # Using ternary operator.
# state = "nice" if is_nice else "not nice"

# # Equivalent code using multi-line if statements.
# if is_nice:
#     state = "nice"
# else:
#     state = "not nice"

# Write a function that uses the ternary operator to return "yeah" if the condition is True, and "nope" otherwise.
# Example:
# yeah_nope(True) ➞ "yeah"
# yeah_nope(False) ➞ "nope"

def yeah_nope(b):
	return "yeah" if b else "nope"
print(yeah_nope(True))
print(yeah_nope(False))