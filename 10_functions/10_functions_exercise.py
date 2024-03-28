# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# ```
# area = (1/2)*base*height
# ```
#

def calculate_area(base, height, shape = "triangle"):
    '''
    :param1 - base of the triangle
    :param2 - height of the triangle
    :param3 - (Optional Parameter) shape of the object. By default it will take as triangle
    :return - area of the object based on the type of shape
    '''
    area = 0
    if shape == "rectangle":
        area = base * height
        print(f"Area of {shape} with length as {base} and width as {height} is {area}")
        return
    area = base/2 * height
    print(f"Area of {shape} with base as {base} and height as {height} is {area}")
    return

# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# ```
# rectangle area=length*width
# ```
# If no shape is supplied then it should take triangle as a default shape

# Calculate area of triangle whose base is 10 and height is 5
calculate_area(10,5,"triangle")

# Calculate area of a rectangle whose length is 20 and width is 30
calculate_area(20,30,"rectangle")

# Calculate area of a triangle without supplying shape argument in a function call
# Here third argument is missing
calculate_area(10,5)


# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
# Not supplying any input will use default argument which is 5
def print_pattern(n=5):
    '''
    :param n - Integer number representing number of lines to be printed in a pattern.Default value for n is 5
    :return: None
    '''
    for i in range(n):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)

print_pattern(10)

