# Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.
# Example:
# long_burp(3) ➞ "Burrrp"
# long_burp(5) ➞ "Burrrrrp"

def long_burp(num):
	return 'Bu' + 'r'*num + 'p'
print(long_burp(3))
print(long_burp(5))