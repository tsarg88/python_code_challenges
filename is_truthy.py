# A "truthy" value is a value that translates to True when evaluated in a Boolean context. All values are truthy unless they're defined as falsy.
# Example:
# is_truthy(0) ➞ 0
# is_truthy(False) ➞ 0
# is_truthy("") ➞ 0
# is_truthy("False") ➞ 1
# is_truthy(True) ➞ 1

def is_truthy(val):
	return 1 if bool(val) == True else 0
print(is_truthy(0))
print(is_truthy(False))
print(is_truthy(""))
print( is_truthy("False"))
print(is_truthy(True))


# method 2
# def is_truthy(val):
#     if bool(val) == True:
#         return 1
#     else:
#         return 0
# print(is_truthy(0))
