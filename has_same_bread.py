# Given two lists, which represent two sandwiches, return whether both sandwiches use the same type of bread. The bread will always be found at the start and end of the list.
# Example:
# has_same_bread(
#   ["white bread", "lettuce", "white bread"],
#   ["white bread", "tomato", "white bread"]
# ) ➞ True
# has_same_bread(
#   ["brown bread", "chicken", "brown bread"],
#   ["white bread", "chicken", "white bread"]
# ) ➞ False

def has_same_bread(lst1, lst2):
	return lst1[0] == lst2[0] and lst1[-1] == lst2[-1]
print(has_same_bread(["white bread", "lettuce", "white bread"],["white bread", "tomato", "white bread"]))
print(has_same_bread(["brown bread", "chicken", "brown bread"],["white bread", "chicken", "white bread"]))