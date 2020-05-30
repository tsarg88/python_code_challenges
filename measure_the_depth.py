# Your goal is to measure the depth of this list, where [] has a depth 1, [[]] has depth of 2, [[[]]] has depth 3, etc.
# Example:
# measure_the_depth([]) ➞ 1
# measure_the_depth([[]]) ➞ 2
# measure_the_depth([[[]]]) ➞ 3
# measure_the_depth([[[[[[[[[[[]]]]]]]]]]]) ➞ 11

# def measure_the_depth(lst):
#     list = str(lst)
#     return list.count('[')
# print( measure_the_depth([]))
# print(measure_the_depth([[]]))
# print(measure_the_depth([[[]]]))
# print(measure_the_depth([[[[[[[[[[[]]]]]]]]]]]))

# method 2
def measure_the_depth(lst):
    return str(lst).count('[')
print( measure_the_depth([]))
print(measure_the_depth([[]]))
print(measure_the_depth([[[]]]))
print(measure_the_depth([[[[[[[[[[[]]]]]]]]]]]))
