# Given a sandwich (as a list), return a list of fillings inside the sandwich. This involves ignoring the first and last elements.
# Example:
# get_fillings(["bread", "ham", "cheese", "ham", "bread"]) ➞ ["ham", "cheese", "ham"]
# get_fillings(["bread", "sausage", "tomato", "bread"]) ➞ ["sausage", "tomato"]

def get_fillings(sandwich):
	return sandwich[1:-1]
print(get_fillings(["bread", "ham", "cheese", "ham", "bread"]))
print(get_fillings(["bread", "sausage", "tomato", "bread"]))