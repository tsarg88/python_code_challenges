# Write a function that takes an integer and returns a string with the given number of "a"s in Edabit.
# Example:
# how_many_times(5) ➞ "Edaaaaabit"
# how_many_times(0) ➞ "Edbit"

def how_many_times(num):
	return 'Ed{}bit'.format(num * 'a')
print(how_many_times(5))
print(how_many_times(0))
	