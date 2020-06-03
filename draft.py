# def is_palindrome(txt):
# 	return True if txt == txt[::-1] else False
# print(is_palindrome("mom"))

def variable_valid(var):
	return True if var.isidentifier() else False
print(variable_valid("esult"))