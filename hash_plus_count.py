# Create a function that returns the number of hashes and pluses in a string.
# Example:
# hash_plus_count("###+") ➞ [3, 1]
# hash_plus_count("##+++#") ➞ [3, 3]

def hash_plus_count(txt):
    count1 = txt.count('#')
    count2 = txt.count('+')
    return [count1, count2]
print(hash_plus_count("###+"))