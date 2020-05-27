# Given a string of what the overlapping claps sounded like, return how many claps('C's) were made in total.
# Example:
# count_claps("ClaClaClaClap!") ➞ 4
# count_claps("ClClClaClaClaClap!") ➞ 6

def count_claps(txt):
	return txt.count('C')
print(count_claps("ClaClaClaClap!"))
print(count_claps("ClClClaClaClaClap!"))