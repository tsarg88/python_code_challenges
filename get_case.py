# Create a function which returns "upper" if all the letters in a word are uppercase, "lower" if lowercase and "mixed" for any mix of the two.
# Example:
# get_case("whisper...") ➞ "lower"
# get_case("SHOUT!") ➞ "upper"
# get_case("Indoor Voice") ➞ "mixed"

# def get_case(txt):
#     if txt == txt.lower():
#         return 'lower'
#     elif txt == txt.upper():
#         return 'upper'
#     else:
#         return 'mixed'
# print(get_case("whisper..."))
# print(get_case("SHOUT!"))
# print(get_case("Indoor Voice"))

# method 2

def get_case(txt):
    return 'upper' if txt.isupper() else 'lower' if txt.islower() else 'mixed'
print(get_case("whisper..."))
print(get_case("SHOUT!"))
print(get_case("Indoor Voice"))
