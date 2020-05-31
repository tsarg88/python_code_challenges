# Andy, Ben and Charlotte are playing a board game. The three of them decided to come up with a new scoring system. A player's first initial ("A", "B" or "C") denotes that player scoring a single point. Given a string of capital letters, return a list of the players' scores.
# For instance, if ABBACCCCAC is written when the game is over, then Andy scored 3 points, Ben scored 2 points, and Charlotte scored 5 points, since there are 3 instances of letter A, 2 instances of letter B, and 5 instances of letter C. So the list [3, 2, 5] should be returned.
# Example:
# calculate_scores("") ➞ [0, 0, 0]
# calculate_scores("A") ➞ [1, 0, 0]
# calculate_scores("ABC") ➞ [1, 1, 1]
# calculate_scores("ABCBACC") ➞ [2, 2, 3]

def calculate_scores(txt):
    return [txt.count('A'),txt.count('B'),txt.count('C')]
print(calculate_scores(""))
print(calculate_scores("A"))
print(calculate_scores("ABC"))
print(calculate_scores("ABCBACC"))

# Method 2:
# def calculate_scores(txt):
# 	a = txt.count('A')
# 	b = txt.count('B')
# 	c = txt.count('C')
	
# 	return [a,b,c]
