# def is_palindrome(txt):
# 	return True if txt == txt[::-1] else False
# print(is_palindrome("mom"))

# def variable_valid(var):
# 	return True if var.isidentifier() else False
# print(variable_valid("esult"))

# def reverse_capitalize(txt):
# 	return txt[::-1].upper()
# print(reverse_capitalize("abc"))

# def ink_levels(inks):
# 	return min(inks.values())
# print(ink_levels({
#   "cyan": 23,
#   "magenta": 12,
#   "yellow": 10
# }))

# def int_within_bounds(n, lower, upper):
# 	if isinstance(n, float):
# 		return False
# 	if n >= lower and n < upper:
# 		return True
# 	else:
# 		return False
# print(int_within_bounds(0, 0, 1))
# print(int_within_bounds(6, 1, 6))
# print(int_within_bounds(4.5, 3, 8))

# def convert(data1, data2):
# 	if type(data1) == list:
# 		return list(data2)
# 	if type(data1) == tuple:
# 		return tuple(data2)
# 	if type(data1) == set:
# 		return set(data2)
# print(convert([1, 2, 4, 8], (7, 8, 9)))
# print(convert((7, 8, 9), [1, 2, 4, 8]))
# print(convert([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}))
# print(convert({2, 3, 5, 7, 11, 13}, [1, 2, 4, 8]))

# def space_me_out(s):
# 	return ' '.join(s)
# print(space_me_out("space"))

# def detect_word(txt):
# 	test = ''
# 	for n in txt:
# 		if n.islower():
# 			test += n
# 			''.join(test)
# 	print(test)
# print(detect_word("UcUNFYGaFYFYGtNUH"))

# def length(s):
# 	total = 0
# 	for i in s:
# 		total += 1
# 	return total
# print(length("Edabit"))

# from math import pi

# def vol_pizza(radius, height):
# 	return round((radius**2) * height * pi)
# print(vol_pizza(15, 1.3))

# def say_hello_bye(name, num):
# 	if num == 1:
# 		return 'Hello' + ' ' + name.title()
# 	if num == 0:
# 		return 'Bye' + ' ' + name.title()
# print(say_hello_bye("alon", 0))

# def score_calculator(easy, med, hard):
# 	if easy < 0 or med < 0 or hard < 0:
# 		return 'invalid'
# 	else:
# 		return (easy * 5) + (med * 10) + (hard * 20) 
# Every operation needs to be in constant time 

import sys
class MinStack(object):
   min=float('inf')
   def __init__(self):
      self.min=float('inf')
      self.stack = []
   def push(self, x):
      if x<=self.min:
         self.stack.append(self.min)
         self.min = x
      self.stack.append(x)
   def pop(self):
      t = self.stack[-1]
      self.stack.pop()
      if self.min == t:
         self.min = self.stack[-1]
         self.stack.pop()
   def top(self):
      return self.stack[-1]
   def getMin(self):
      return self.min
m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
# print(m.getMin())
# m.pop()
# print(m.top())
# print(m.getMin())
print(m.top())