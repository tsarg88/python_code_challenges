# The important thing when a comment is posted on Edabit is its content. But when a comment is formatted in the right way, it will be properly shown and it will be easily readable by everyone.

# In this challenge, you have to format a word using four specific methods of the Markdown language that is used by Edabit to format the text in the Comments tab and the Instructions tab (during the creation, or the translation, of a challenge). Each of these four methods (or styles) is identified by the lowercased initial letter of its name:

# "b" is for bold
# "i" is for italics
# "c" is for inline code
# "s" is for strikethrough
# You are given two parameters: a string word being the word to format, and another string style being the lowercased initial of the style to apply. You have to implement a function that returns a string being the word surrounded by the special characters used to apply the given style.
# Examples:
# md_format("Bold", "b") --> "**Bold**
# md_format("Italics", "i") --> "_Italics_"
# md_format("Code", "c") --> "`Code`"
# md_format("Ruby", "s") --> "~~Ruby~~"

def md_format(word, style):
	markdown = {
    'b':'**', 
    'i':'_', 
    'c':'`', 
    's':'~~'}
	return '{0}{1}{0}'.format(markdown[style], word)
print(md_format("Bold", "b"))
print(md_format("Italics", "i"))
print(md_format("Code", "c"))
print(md_format("Ruby", "s"))

# Method 2
# def md_format(word, style):
#     if style == "b":
#         return "**{}**".format(word)
#     elif style == "i":
#         return "_{}_".format(word)
#     elif style== "c":
#         return "`{}`".format(word)
#     else:
#         return "~~{}~~".format(word)
        