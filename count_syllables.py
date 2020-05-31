# Create a function that returns the number of syllables in a simple string. The string is made up of short repeated words like "Lalalalalalala" (which would have 7 syllables).
# Examples:
# count_syllables("Hehehehehehe") ➞ 6
# count_syllables("bobobobobobobobo") ➞ 8
# count_syllables("NANANA") ➞ 3

def count_syllables(txt):
	return sum(1 for i in txt.lower() if i in 'aeiou')
print(count_syllables("Hehehehehehe"))
print(count_syllables("bobobobobobobobo"))
print(count_syllables("NANANA"))
