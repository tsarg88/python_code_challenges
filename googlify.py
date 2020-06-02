# Google's logo can be stretched depending on how many pages it lets you skip forward to.
# Let's say we wanted to change the amount of pages that Google could skip to. Create a function where given a number of pages n, return the word "Google" but with the correct number of "o"s.
# Note:
# If n is equal to or less than 1, return invalid.
# Example:
# googlify(10) ➞ "Goooooooooogle"
# googlify(23) ➞ "Gooooooooooooooooooooooooogle"
# googlify(2) ➞ "Google"
# googlify(-2) ➞ "invalid"

def googlify(n):
	return 'G{}gle'.format('o' * n) if n > 1 else 'invalid'
print(googlify(10))
print(googlify(23))
print(googlify(2))
print(googlify(-2))
