# Create a function that counts the number of syllables a word has. Each syllable is separated with a dash -.
# Example:
# number_syllables("buf-fet") ➞ 2
# number_syllables("beau-ti-ful") ➞ 3

def number_syllables(word):
    return len(word.split('-'))
print(number_syllables("buf-fet"))
print(number_syllables("beau-ti-ful"))