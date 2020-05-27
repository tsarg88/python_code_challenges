# Create a function which validates whether a bridge is safe to walk on (i.e. has no gaps in it to fall through).
# Example:
# is_safe_bridge("####") ➞ True
# is_safe_bridge("## ####") ➞ False

def is_safe_bridge(s):
	if ' ' in s:
		return False
	else:
		return True
print(is_safe_bridge("####"))
print(is_safe_bridge("## ####"))
