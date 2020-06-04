# Create a function that takes three parameters and returns a list with the first parameter x, the second parameter y, and every number in between 
# the first and second parameter in ascending order. Then filter through the list and return the list with numbers that are only divisible by 
# the third parameter n.
# Notes:
# The final list should consist of all numbers between x and y inclusive that are divisible by n.
# Return an empty list if there are no numbers that are divisible by n.
# Example:
# list_operation(1, 10, 3) ➞ [3, 6, 9]
# list_operation(7, 9, 2) ➞ [8]
# list_operation(15, 20, 7) ➞ []

def list_operation(x, y, n):
    range_list = range(x, y + 1)
    main_list = []
    for i in range_list:
        # print(i)
        if i % n == 0:
            main_list.append(i)
    return main_list
print(list_operation(1, 10, 3))
print(list_operation(7, 9, 2))
print(list_operation(15, 20, 7))
