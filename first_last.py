# Create a function that takes a list of elements and return the first and last elements as a new list.
# Example:
# first_last([5, 10, 15, 20, 25]) ➞ [5, 25]
# first_last(["edabit", 13, None, False, True]) ➞ ["edabit", True]

def first_last(lst):
    return [lst[0], lst[1]]
print(first_last([5, 10, 15, 20, 25]))
print(first_last(["edabit", 13, None, False, True]))

