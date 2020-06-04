# A word is on the loose and now has tried to hide amongst a crowd of tall letters! Help write a function to detect what the word is, knowing the following rules:

# The wanted word is in lowercase.
# The crowd of letters is all in uppercase.
# Note that the word will be spread out amongst the random letters, but their letters remain in the same order.

# Example:
# detect_word("UcUNFYGaFYFYGtNUH") ➞ "cat"
# detect_word("bEEFGBuFBRrHgUHlNFYaYr") ➞ "burglar"
# detect_word("YFemHUFBbezFBYzFBYLleGBYEFGBMENTment") ➞ "embezzlement"


def detect_word(txt):
    return "".join(i for i in txt if i.islower())
print(detect_word("UcUNFYGaFYFYGtNUH"))
print(detect_word("bEEFGBuFBRrHgUHlNFYaYr"))
print(detect_word("YFemHUFBbezFBYzFBYLleGBYEFGBMENTment"))
	