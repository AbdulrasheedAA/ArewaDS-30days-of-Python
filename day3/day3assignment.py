import math

# Task 1 - 3
my_age = int(29)
my_height = float(5.9)
complex_number = 2 + 3j

print(type(my_age))
print(type(my_height))
print(type(complex_number))

# Task 4
base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
triangle_area = 0.5 * base * height
print(f"The area of the triangle is {triangle_area}")

# Task 5
side_a = float(input("Enter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))
triangle_perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {triangle_perimeter}")

# Task 6
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
print(f"The area of the rectangle is {rectangle_area}")
print(f"The perimeter of the rectangle is {rectangle_perimeter}")

# Task 7
radius = float(input("Enter the radius of the circle: "))
circle_area = math.pi * radius**2
circle_circumference = 2 * math.pi * radius
print(f"The area of the circle is {circle_area}")
print(f"The circumference of the circle is {circle_circumference}")

# Task 8
# Equation: y = 2x - 2
# from the equation y = mx + b 
# where: m coefficient of x is the slope,
#        b constant is the y intercept
# x intercept is obtain by equating y to 0
#   therefore: the quation become 0 = 2x - 2
#    x = 1
slope = 2
x_intercept = 1
y_intercept = -2
print(f"Slope: {slope}, X-Intercept: {x_intercept}, Y-Intercept: {y_intercept}")

# Task 9
# Calculate slope and Euclidean distance
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_9 = (y2 - y1) / (x2 - x1)
euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Slope: {slope_9}, Euclidean Distance: {euclidean_distance}")

# Task 10
# Compare slopes
if slope == slope_9:
    print("The slopes are equal.")
else:
    print("The slopes are not equal.")

# Task 11
# Calculate y values
x_values = [1, 2, 3, 4, 5]
for x_value in x_values:
    y_value = x_value**2 + 6*x_value + 9
    print(f"For x = {x_value}, y = {y_value}")

# Task 12
# Falsy comparison statement
length_python = len('python')
length_dragon = len('dragon')
print(f"The length of 'python' is {length_python} and 'dragon' is {length_dragon}.")
print(f"The statement 'Length of python is not equal to length of dragon' is {length_python != length_dragon}.")

# Task 13
# Check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print("'on' is found in both 'python' and 'dragon'.")
else:
    print("'on' is not found in both 'python' and 'dragon'.")

# Task 14
# Check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon"
if 'jargon' in sentence:
    print("'jargon' is in the sentence.")
else:
    print("'jargon' is not in the sentence.")

# Task 15


# Task 16
# Convert the length of 'python' to float and then to string
length_python_float = float(length_python)
length_python_str = str(length_python_float)
print(f"The length of 'python' as a float is {length_python_float} and as a string is {length_python_str}.")

# Task 17
# Check if a number is even or not
number = input('Enter any number: ')
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is not an even number.")

# Task 18
# Check if floor division of 7 by 3 is equal to the int converted value of 2.7
if 7 // 3 == int(2.7):
    print("The floor division of 7 by 3 is equal to the int converted value of 2.7.")
else:
    print("The condition is not met.")

# Task 19
# Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print("The types are equal.")
else:
    print("The types are not equal.")

# Task 20
# Check if int('9.8') is equal to 10
try:
    value = int('9.8')
    if value == 10:
        print("The conversion and comparison were successful.")
    else:
        print("The comparison failed.")
except ValueError:
    print("The conversion failed. '9.8' is not a valid integer.")

# Task 21
# Calculate pay based on hours and rate per hour
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print(f"Your weekly earning is {weekly_earning}")

# Task 22
# Calculate the number of seconds a person can live
years_lived = float(input("Enter number of years you have lived: "))
seconds_in_a_year = 60 * 60 * 24 * 365
total_seconds_lived = years_lived * seconds_in_a_year
print(f"You have lived for {total_seconds_lived} seconds.")

# Task 23
# Display the table
for i in range(1, 6):
    print(f"{i} {1} {i} {i**2} {i**3}")