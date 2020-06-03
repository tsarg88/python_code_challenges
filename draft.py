def is_palindrome(txt):
	return True if txt == txt[::-1] else False
print(is_palindrome("mom"))