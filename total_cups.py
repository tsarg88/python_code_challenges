# Per 6 coffee cups I buy, I get a 7th cup free. In total, I get 7 cups. Create a function that takes n cups bought and return the total number of cups I would get.
# Example:
# total_cups(6) ➞ 7
# total_cups(12) ➞ 14

def total_cups(n):
	x = n // 6
	return n + x
print(total_cups(6))
print(total_cups(12))

