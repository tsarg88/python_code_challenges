# Create a function that returns True if an input string contains only uppercase or only lowercase letters.
# Example:
# same_case("hello") ➞ True
# same_case("HELLO") ➞ True
# same_case("Hello") ➞ False

def same_case(txt):
 return txt.islower() or txt.isupper()
print(same_case("hello"))
print(same_case("Hello"))