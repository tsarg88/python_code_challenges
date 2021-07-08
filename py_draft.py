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

# import sys
# class MinStack(object):
#    min=float('inf')
#    def __init__(self):
#       self.min=float('inf')
#       self.stack = []
#    def push(self, x):
#       if x<=self.min:
#          self.stack.append(self.min)
#          self.min = x
#       self.stack.append(x)
#    def pop(self):
#       t = self.stack[-1]
#       self.stack.pop()
#       if self.min == t:
#          self.min = self.stack[-1]
#          self.stack.pop()
#    def top(self):
#       return self.stack[-1]
#    def getMin(self):
#       return self.min
# m = MinStack()
# m.push(-2)
# m.push(0)
# m.push(-3)
# print(m.getMin())
# m.pop()
# print(m.top())
# print(m.getMin())
# print(m.top())

# def add_ending(lst, ending):
# 	return [i + ending for i in lst]
# print(add_ending(["clever", "meek", "hurried", "nice"], "ly"))

# def is_identical(s):
# 	n = len(s)
# 	for i in range(1, n):
# 		if s[i] != s[0]:
# 			return False
# 	return True
# print(is_identical("aaanaa"))

# def is_in_range(n, r):
# 	if n >= r['min'] and n <= r['max']:
# 		return True
# 	return False
# print(is_in_range(6, { "min": 0, "max": 5 }))

# def unlucky_13(nums):
# 	return [num for num in nums if num%13 != 0]
# # print(unlucky_13([53, 182, 435, 591, 637]))
# # print(unlucky_13([24, 316, 393, 458, 1279]))
# print(unlucky_13([104, 351, 455, 806, 871]))

# def reverse_title(txt):
# 	return txt.title().swapcase()
# print(reverse_title("this is a title"))

# def add_odd_to_n(n):
# 	sum = 0
# 	for x in range(n+1):
# 		if(x % 2 != 0):
# 			sum = sum + x
# 	return sum
# print(add_odd_to_n(4))

# def get_triangle_type(lst):
# 	s = set(lst)
# 	return 'not a triangle' if len(lst)!=3\
# 		else 'equilateral' if len(s)==1\
# 		else 'isosceles' if len(s)==2\
# 		else 'scalene'
# print(get_triangle_type([3, 1, 2]))

# def removeElement(nums, val):
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] != val :
#                 nums[count] = nums[i]
#                 count +=1
#         return nums
# print(removeElement([3,2,2,2,3,4,5], 2))

# def checkSquareAndCube(arr):
#         total = []
#         for i in arr:
#             print(i)

# print(checkSquareAndCube([16, 48]));

# def isPlural(word):
#     print(word[-1])
# print(isPlural("changes"))

# def pairs(k, arr):
#     count = 0
#     for i in range(0, len(arr)):
#         print('tyusi loop', arr[i])
#         for j in range(i+1, len(arr)):
#             print('mechi loop', arr[j])
#             if arr[j] - arr[i] == k:
#                 count += 1
#     return count
# print(pairs (2, [1, 2, 3, 4, 5]))

# def hash_pairs(k, arr):
#     complement = set(arr)
#     count = 0
#     for i in arr:
#         print(i)
#     #     target = i - k
#     #     if target in complement:
#     #         count+=1
#     # return count


# print(hash_pairs (2, [1, 2, 3, 40]))

# def test():
#     list = [1, 2, 30]
#     for i in list:
#         print(i)
# print(test())

# def pairs(k, arr):
#     cnt = 0
#     s = set(arr)
#     arr = list(s)[::-1]
#     for x in arr:
#         if x - k in s:
#             cnt+=1
#     return cnt
# print(pairs (2, [1, 2, 3, 4])) 

# def binary_search(target, arr):
#     # find pivot
#     pivot = len(arr) // 2
#     if arr[pivot] == target:
#         return True
#     if len(arr) == 1:
#         return False

#     if arr[pivot] < target:
#         # take left side
#         return binary_search(target, arr[:pivot])
    
#     if arr[pivot] > target:
#         return binary_search(target, arr[pivot+1:])

# def search_pairs(arr, target):
#     arr.sort()
#     total = 0
#     for item in arr:
#         complement = item - target
#         if binary_search(complement, arr):
#             total += 1
#     return total
# print(search_pairs([1, 2, 3, 4], 2)) 


# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.
 
# Returns index of x in arr if present, else -1
# def binary_search(arr, low, high, x):
#     print( '-1 index test', arr[0:-1] )
 
#     # Check base case
#     if high >= low:
 
#         mid = (high + low) // 2
 
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
 
#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
 
#         # Else the element can only be present in right subarray
#         else:
#             return binary_search(arr, mid + 1, high, x)
 
#     else:
#         # Element is not present in the array
#         return -1
 
# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 3
 
# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)
# # print('arr length', len(arr))
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")
# ------------------------------------------------------------------------------------------------
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
 
#     while low <= high:
 
#         mid = (high + low) // 2
 
#         # If x is greater, ignore left half
#         if arr[mid] < x:
#             low = mid + 1
 
#         # If x is smaller, ignore right half
#         elif arr[mid] > x:
#             high = mid - 1
 
#         # means x is present at mid
#         else:
#             return "The searched element is in the index of {index} with the value of {value} ".format(index = mid, value=arr[mid])
 
#     # If we reach here, then the element was not present
#     return -1
 
 
# # Function call
# print(binary_search([ 2, 3, 4, 10, 40 ], 10))


# def recur_fibo(n):  
#    if n == 1:  
#        return 0
#    if n == 2:
#        return 1  
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
# print(recur_fibo(5))  



# def superDigit(n, k):
    # create super_n which will hold the value of n
    # super_n = superDigitRecursive(n)
    # create the p which will hold n * k(n concatenated k times)
    # p = super_n * k
    # call superDigitRecursive on p
    # return superDigitRecursive(str(p))

# def superDigitRecursive(n: str):
#     # base case
#     # if n is a single digit
#         # return n
#     if len(str(n)) == 1:
#         return int(n)
     
#       # iterate over n
#         # sum the digits together
#         # each digit is a str
#         # convert each digit to a str
#     n_sum = 0
#     for digit in str(n):
#         print(digit)
#         n_sum += int(digit)

  

#     # call out recursive function on the sum(as a str)
#     return superDigitRecursive(str(n_sum))
# print(superDigit(154, 2))



# def stepPerms(n):
#         cache = {0:1, 1:1, 2:2}
#         def stairs(n):
#             if n in cache:
#                 return cache[n]
#             cache[n] = stairs(n-1) + stairs(n-2) + stairs(n-3)
#             return cache[n]
#         return stairs(n)
# print(stepPerms(3))

# def stepPerms(n):
#     arr = [1,1,2]
    
#     for i in range(3, n+1):
#       arr.append(arr[i-1] + arr[i-2] + arr[i-3])
#     return arr[n]
# print(stepPerms(4))

# def rotLeft(a, d):
#    total = []
#    test = slice(1, 5)
#    for i in range(1, a+1):
#        total.append(i)
#    print(total[test])
# print(rotLeft(5, 4))

# def isCryptSolution(crypt, solution):
#     # crypt_s = crypt
#     for i in range(0, 3):
#         # print(i)
#         for s in solution:
#             # print(s)
#             crypt[i] = crypt[i].replace(s[0], s[1])
#             print(crypt[i])
        
#         if crypt[i] != '0' and crypt[i][0] == '0':
#             return False
        
#     if int(crypt[0]) + int(crypt[1]) != int(crypt[2]):
#         return False
#     # print(crypt)
#     return True
# print(isCryptSolution(["AAA"],
#       [["A","0"]]   ))
    #   321

# Definition for singly-linked list:
# class ListNode():
#   def __init__(self, value):
#     self.value = value
#     self.next = None

#     def removeKFromList(l, k):
#         curr = l
#         while curr:
#             if curr.next and curr.next.value == k:
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next
#         return l if (l is None or l.value != k) else l.next
    
# listNode = ListNode()
# listNode.add('a')
# print(listNode)


# Sorting using stack data structure

# class Stack:
#     def __init__(self):
#         self.storage = []

#     def push(self, item):
#         self.storage.append(item)
    
#     def pop(self):
#         return self.storage.pop()

#     def peak(self):
#         return self.storage[-1]

#     def is_empty(self):
#         return len(self.storage) == 0

#     def print_contents(self):
#         for item in self.storage:
#             print(item)

# def sort_stack(input_stack):   
#     # init second stack
#     output_stack = Stack()
#     # loop until the first stack is empty
#     # also make surethat we don't leave anything in temp
#     temp = None
#     while input_stack.is_empty() == False:
#         # put the top of the first stack in a temp var
#         if temp is None:
#             temp = input_stack.pop()
#         # if the second stack is empty OR temp > the top of the second stack
#         if output_stack.is_empty() or temp > output_stack.peak():
#             # push temp to the second stack
#             output_stack.push(temp)
#             temp = None
#         # else:
#         else:
#             # pop the top of the second stack and push to the first
#             input_stack.push(output_stack.pop())
    
#     return output_stack

# s = Stack()
# s.push(4)
# s.push(10)
# s.push(8)
# s.push(5)
# s.push(1)
# s.push(6)

# sorted_stack = sort_stack(s)
# sorted_stack.print_contents()


# def truckTour(petrolpumps):
#     start = 0
#     current = 0
#     tank = 0
#     while start < len(petrolpumps):
#         tank += petrolpumps[current][0]
#         tank -= petrolpumps[current][1]
#         current = (current + 1) % len(petrolpumps)
#         if tank < 0:
#             tank = 0
#             start = current
#         elif current == start:
#             return start
# print(truckTour([[1, 5], [10, 3], [3, 4]]
# ))

# def twoStrings(s1, s2):
#     # creating set/hash
#     hash = set()
#     # iterate over the first string
#     for char in s1:
#         # add each character to hash set
#         hash.add(i)
#     # iterate over the second string
#     for char in s2:
#         # if we find a match in the first hash set
#         if i in hash:
#             # return Yes
#             return 'YES'
#     return 'NO'
# print(twoStrings("rdvrk", "apple"))

# def getAllSubstrings(s):
#     # return all substrings of a given string
#     # get all the one letter, then 2 letter, then 3 letter etc..
#     subs = []
#     for i in range(len(s)):
#         for j in range(i+1, len(s)+1):
#             subs.append(s[i:j])
#     return subs
# print(getAllSubstrings('thing'))


# finding mergeing node in linked list
def findMergeNode(head1, head2):
    # find the length of the two lists
    length1 = get_length(head1)
    length2 = get_length(head2)

    # move head of the larger list difference of the two lists
    if length1 > length2:
        diff = length1 - length2
        for i in range(diff):
            head1 = head1.next

    if length2 > length1:
        diff = length2 - length1
        for i in range(diff):
            head2 = head2.next

    # iterate over the two lists at the same time 
    while head1 or head2:
        # compare the nodes
        # if they're equal , we've found the merge point
        if head1 == head2:
            return head1.data

        head1 = head1.next
        head2 = head2.next


# function for getting the length of the lists
# def get_length(head):
#     length = 0
#     curr = head
#     while curr is not None:
#         length += 1
#         curr = curr.next
#     return length

# def stutter(word):
# 	return "{s}... {s}... {w}?".format(s=word[0:2], w=word)
# print(stutter("incredible"))

# def is_curzon(num):
#     a = 2 ** num + 1
#     b = 2 * num + 1
#     if a % b == 0:
#         return True
#     return False

# print(is_curzon(10))


# def radians_to_degrees(rad):
#     # r = 57.3
#     # result = r * rad
#     # return round(result)
#     print(round(57.3, 1))
# print(radians_to_degrees(60))

# def countVowels(string):
#    vowels = ['a','e','i','o','u']
#    total = 0
#    for s in string:
#       if s in vowels:
#          total += 1
#    return total

# def relation_to_luke(name):
#     dic = {"Darth Vader":"father", "Leia":"sister", "Han":"brother in law", "R2D2":"R2D2"}             
#     return "Luke, I am your {f}.".format(f=dic[name])
# print(relation_to_luke("Darth Vader"))

# def time_for_milk_and_cookies(date):
# 	return "12, 24" in date
# print(time_for_milk_and_cookies("2021, 13, 24"))

# def factorial(num):
#     import math
#     return math.factorial(num)
# print(factorial(5))

# class LinkedList:
#     def __init__(self, item=None):
#         self.next = None
#         self.val = item

#     def __len__(self):
#         cur = self
#         count = 1 if self.val is not None else 0
#         while cur.next is not None:
#             count += 1
#             cur = cur.next
#         return count    

#     def append(self, item):
#         if not self.val:
#             self.val = item
#             return

#         cur = self
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = LinkedList(item)

# myList = LinkedList()
# myList.append('a')
# myList.append('b')
# myList.append('c')
# print(len(myList))

# class ListNode(object):
#    def __init__(self, x):
#      self.value = x
#      self.next = None

# def createList(lst):
#         head = None
#         for val in lst:
#             node = ListNode(val)
#             node.next = head
#             head = node
#         return head

# def iter(head):
#     while head:
#         yield head.value
#         head = head.next

# def removeKFromList(l, k):
#      c = l
#      while c:
#          if c.next and c.next.value == k:
#              c.next = c.next.next
#          else:
#              c = c.next
#      return l.next if l and l.value == k else l

# define the input
# l = createList([3, 1, 2, 3, 4, 5, 3])
# k = 3  
# run your algorithm
# result = removeKFromList(l, 3)
# verify it
# print(*iter(result)) 

# class ListNode(object):
#    def __init__(self, x):
#      self.value = x
#      self.next = None

# def removeKFromList(l, k):
#     c = l
#     while c:
#         if c.next and c.next.value == k:
#             c.next = c.next.next
#         else:
#             c = c.next
#     return l.next if l and l.value == k else l

# l = ListNode(3)
# l.next = ListNode(1)
# print(*iter(l)) 

  

# def test(n):
#     yield n
# print(test(7))

# matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]
# def is_adjacent(matrix, node1, node2):
#     print(matrix[1][0])
#     # if matrix[0][1] == 1:
#     #     return "qsd"
#     # else:
#     #     return False
#     # return matrix[node1][node2] == 1

# print(is_adjacent(matrix, 0, 3))

# def solutions(a, b, c):
# 	if pow(b, 2) > 4 * a * c:
# 		return 2
# 	elif pow(b, 2) < 4 * a * c:
# 			return 0
# 	else:
# 		return 1
# print(solutions(1, 0, 0))

# import math
# def is_sastry(n):
#     total = str(n) + str(n + 1)
#     if (math.ceil(math.sqrt(int(total))) == math.floor(math.sqrt(int(total)))):
#         return True
#     return False
# print(is_sastry(10))

# import math
# def is_sastry(n):
#     # print(math.ceil(n))
#     print(math.ceil(math.sqrt(n)))
#     if (math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n))):
#         return True
#     return False
# print(is_sastry(10))

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
# print(factorial(4))

# def sum_fractions(lst):
#     print(round(3.4))
#     # total = 0
#     # for i in lst:
#     #     total += i[0] / i[1]
#     #     return round(total, 0)
# print(sum_fractions([[18, 13], [4, 5]]))

# def box_seq(step):
# 	if step == 0:
# 		return 0
# 	if step % 2 == 0:
# 		return step
# 	else:
# 		return step+2

# print(box_seq(3))

# def dna_to_rna(dna):
#     translation = {65: 85, 84: 65, 71: 67, 67: 71}
#     return dna.translate(translation)
# print(dna_to_rna("ATTAGCGCGATATACGCGTAC"))

# def age_difference(f_age, s_age):
#     if f_age % s_age == 0:
#         return 0
#     else:

# print(age_difference(42, 21))

# def fizz_buzz(maximum):
#     list = []
#     for i in range(1, maximum+1):
#         if i % 3 == 0 and i % 5 == 0:
#             list.append("FizzBuzz")
#         elif i % 3 == 0:
#             list.append("Fizz")
#         elif i % 5 == 0:
#             list.append("Buzz")
#         else:
#             list.append(i)
#     return list
# print(fizz_buzz(15))

# def largest_even(lst):
#     total = []
#     for i in lst:
#         if i % 2 == 0:
#             total.append(i)
#     if len(total) == 0:
#         return -1
#     else:
#         return total[-1]
        
   
# print(largest_even([3, 7, 5]))

# def face_interval(num):
#     if type(num) is str:
#         return ":/"
#     difference = max(num) - min(num)
#     if difference in num:
#         return ":)"
#     else:
#         return ":("

# print(face_interval("sd"))

# Create a function that takes in a list of intervals and returns how many intervals overlap with 
# a given point.
# An interval overlaps a particular point if the point exists inside the interval, or on the interval's 
# boundary. For example the point 3 overlaps with the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary).

# To illustrate:
# count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2) ➞ 3
# # Since [1, 2], [2, 3] and [1, 3] all overlap with point 2
# Examples
# count_overlapping([[1, 2], [2, 3], [3, 4]], 5) ➞ 0
# count_overlapping([[1, 2], [5, 6], [5, 7]], 5) ➞ 2
# count_overlapping([[1, 2], [5, 8], [6, 9]], 7) ➞ 2

# def count_overlapping(intervals, point):
#     total = 0
#     for i in intervals:
#         if point >= i[0] and point <= i[1]:
#             total += 1
#     return total
# print(count_overlapping([[1, 2], [5, 6], [5, 7]], 5) )

# using map with lambda
# numbers = (1, 2, 3, 4)
# result = map(lambda v: v * v, numbers)
# print(list(result))

# Create a function that takes in a list of tuples as input, and return John's score after his game has ended.
# Examples
# dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21
# dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0
# dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27
def dice_game(lst):
    total = 0
    for a, b in lst:
        if a == b:
            return 0
        else:
            total += a+b
    return total
print(dice_game([(1, 2), (3, 4), (5, 6)]))