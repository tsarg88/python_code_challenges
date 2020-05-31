# Given a class for a BasicPlan, write the classes for StandardPlan and PremiumPlan which have class attributes of the following:
# Examples:
# BasicPlan.has_SD ➞ True
# PremiumPlan.has_SD ➞ True
# BasicPlan.has_UHD ➞ False
# BasicPlan.price ➞ "$8.99"
# PremiumPlan.num_of_devices ➞ 4

class BasicPlan:
	can_stream = True
	can_download = True
	num_of_devices = 1
	has_SD = True
	has_HD = False
	has_UHD = False
	price = '$8.99'
	
# Write the classes for StandardPlan and PremiumPlan here!
class StandardPlan:
	can_stream = True
	can_download = True
	num_of_devices = 2
	has_SD = True
	has_HD = True
	has_UHD = False
	price = '$12.99'
	
class PremiumPlan:
	can_stream = True
	can_download = True
	num_of_devices = 4
	has_SD = True
	has_HD = True
	has_UHD = True
	price = '$15.99'

print(BasicPlan.has_SD)
print(PremiumPlan.has_SD)
print(BasicPlan.has_UHD)
print(BasicPlan.price)
print(PremiumPlan.num_of_devices)
