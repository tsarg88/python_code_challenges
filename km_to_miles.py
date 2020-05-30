# In this challenge, you have to implement a function that returns the given distance kilometers converted into miles. You have to round the result up to the fifth decimal digit.
# Example:
# km_to_miles(2) ➞ 1.24274
# km_to_miles(6) ➞ 3.72823

def km_to_miles(kilometers):
	return round(kilometers * 0.621371, 5)
print(km_to_miles(2))
print(km_to_miles(6))
