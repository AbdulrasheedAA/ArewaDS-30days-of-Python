# Day 2: Variables, Builtin Functions

# Excercise Level 1
firstname = 'Abdulrasheed'
lastname = 'Abdulraheem'
full_name = firstname + ' ' +lastname
country = 'Nigeria'
city = 'Lagos'
age = '29'
year = '2023'
is_married = True
is_true = True
is_light_on = True
qualification, course, school = 'B.Sc.', 'Surveying and Geoinformatics', 'University of Ilorin'


print("First Name:", firstname)
print("Last Name:", lastname)
print("Full Name:", full_name)
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Year:", year)
print("Married:", is_married)
print("True:", is_true)
print("Light On:", is_light_on)
print("Multiple Variables:", qualification, course, school)


# Excercise Level 2

print(type(firstname))
print(type(lastname))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print('')

print(len(firstname))
print('Length of First name is ', len(firstname))
print('Length of Last name is ', len(lastname))

print('Length of First name > Length of Last name')

print('')

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
Floor_division = num_one // num_two

print('First number:', num_one)
print('Second number:', num_two)
print('Total:', total)
print('Difference:', diff)
print('Product:', product)
print('Division:', division)
print('Remainder:', remainder)
print('Exponential:', exp)
print('Floor Division:', Floor_division)

print('')
# Area of Circle
print('Calculate Area and Circumference of a Circle with radiu = 30 meters')
import math
radius = 30
area_of_circle = round(math.pi * radius**2, 3)
circum_of_circle = round(2 * math.pi * radius, 3)
print("Area of the circle:", area_of_circle, ' Square meters')
print("Circumference of the circle:", circum_of_circle, 'meters')

print('')
user_radius = float(input("Enter the radius of the circle (in meters): "))
user_area_of_circle = round(math.pi * (user_radius ** 2), 3)
print("Area =", user_area_of_circle, 'Square Meters')

print('')

print('User input Data')

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
age = int(age)
print('')
print('User input Data')
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

help('keyword')