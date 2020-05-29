# Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.
# Example:
# char_count("c", "Chamber of secrets") ➞ 1
# char_count("b", "big fat bubble") ➞ 4

def char_count(txt1, txt2):
	return txt2.count(txt1)
print(char_count("c", "Chamber of secrets"))
print(char_count("b", "big fat bubble"))