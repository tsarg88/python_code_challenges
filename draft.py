# def is_palindrome(txt):
# 	return True if txt == txt[::-1] else False
# print(is_palindrome("mom"))

# def variable_valid(var):
# 	return True if var.isidentifier() else False
# print(variable_valid("esult"))

# def reverse_capitalize(txt):
# 	return txt[::-1].upper()
# print(reverse_capitalize("abc"))

# def ink_levels(inks):
# 	return min(inks.values())
# print(ink_levels({
#   "cyan": 23,
#   "magenta": 12,
#   "yellow": 10
# }))

# def int_within_bounds(n, lower, upper):
# 	if isinstance(n, float):
# 		return False
# 	if n >= lower and n < upper:
# 		return True
# 	else:
# 		return False
# print(int_within_bounds(0, 0, 1))
# print(int_within_bounds(6, 1, 6))
# print(int_within_bounds(4.5, 3, 8))

# def convert(data1, data2):
# 	if type(data1) == list:
# 		return list(data2)
# 	if type(data1) == tuple:
# 		return tuple(data2)
# 	if type(data1) == set:
# 		return set(data2)
# print(convert([1, 2, 4, 8], (7, 8, 9)))
# print(convert((7, 8, 9), [1, 2, 4, 8]))
# print(convert([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}))
# print(convert({2, 3, 5, 7, 11, 13}, [1, 2, 4, 8]))

# def space_me_out(s):
# 	return ' '.join(s)
# print(space_me_out("space"))

def detect_word(txt):
	test = ''
	for n in txt:
		if n.islower():
			test += n
			''.join(test)
	print(test)
print(detect_word("UcUNFYGaFYFYGtNUH"))