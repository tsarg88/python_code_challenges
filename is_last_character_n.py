# Create a function that takes a string (a random name). If the last character of the name is an "n", return True, otherwise return False.
# Example:
# is_last_character_n("Aiden") ➞ True
# is_last_character_n("Piet") ➞ False

def is_last_character_n(word):
	return word.endswith('n')
print(is_last_character_n("Aiden"))
print(is_last_character_n("Roxy"))