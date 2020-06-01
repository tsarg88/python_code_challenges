# Create a function that takes a whole number as input and returns the shape with that number's amount of sides. Here are the expected outputs to get from these inputs.
# Inputs	Outputs
# 1	"circle"
# 2	"semi-circle"
# 3	"triangle"
# 4	"square"
# 5	"pentagon"
# 6	"hexagon"
# 7	"heptagon"
# 8	"octagon"
# 9	"nonagon"
# 10 "decagon"
# Example:
# n_sided_shape(3) ➞ "triangle"
# n_sided_shape(1) ➞ "circle"
# n_sided_shape(9) ➞ "nonagon"

def n_sided_shape(n):
    shapes = {
        1: "circle",
		2: "semi-circle",
		3: "triangle",
		4: "square",
		5: "pentagon",
		6: "hexagon",
		7: "heptagon",
		8: "octagon",
		9: "nonagon",
		10: "decagon"
    }
    return shapes[n]
print(n_sided_shape(3))
print(n_sided_shape(1))
print(n_sided_shape(9))
