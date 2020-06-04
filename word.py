# Create a function that returns a number, based on the string provided. Here is a list of all digits (if you are non english speaker):
# From 1 to 10
# Example:
# word("one") ➞ 1
# word("two") ➞ 2
# word("nine") ➞ 9

def word(s):
    main = {'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9,'ten': 10}
    return main.get(s)
print(word("one"))
print(word("two"))
print(word("nine"))
