# Day 8 Assignment : Dictionaries

# 1. creating empty dictionary called dog
dog = {}
print(dog)

# 2. Adding items to dog
dog = {'name':'Bingo',
       'color':'Brown',
       'Breed': 'German Shepherd',
       'legs': 'four',
       'age': 'Eight years'
       }
print('Dog Info:')
print('Name:', dog['name'])
print('Breed:', dog['Breed'])
print('Age:', dog['age'])
print('Color:', dog['color'])
print('legs:', dog['legs'])

print()
# 3. Create student dictionary

student ={'first_name': 'Isah', 
          'last_name' : 'Musa', 
          'gender' : 'Male',
           'age' : '25', 
           'marital_status':'Single', 
           'skills' : ['Java', 'HTML', 'Python', 'SQL'], 
           'country': 'Nigeria', 
           'city':'Lagos',
           'address': {'house_no': '18', 
                       'street':'Rasaki Taiwo',
                         'city':'Lagos', 
                         'zip_code':'100201'}
                         
            }

print('Student Info:-')
print('First name:', student['first_name'])
print('Last name:', student['last_name'])
print('Gender:', student['gender'])
print('Age:', student['age'])
print('Marital Satus:', student['marital_status'])
print('Skils:', student['skills'])
print('Country:', student['country'])
print('City:', student['city'])
print('Address:', student['address']['house_no'],',' , student['address']['street'],',', student['address']['city'])

print()
# 4. Length of Student Dictionary
print('Length of Student dictionary:', len(student))

print()
# 5. Get value of Skills and Checking Data type
skills = student.get('skills')
print("Student's Skills:", skills)
print('Data type:', type('skills'))

print()

# 6. Modifying the skills values 
add_skills = ['UX', 'R', 'React']
student['skills'].extend(add_skills)

print("Updated Student's Skills:", student['skills'])

print()

# 7. Get Dictionary keys as a list
keys = student.keys()
print(keys)

print()

# 8. Get dictionary values as a list
values = student.values()
print(values)

print()

# 9. Change Dictionary to a list of tuples
print(student.items())

print()

# 10. Deleting an item in the dictionary
del(student['address'])
print(student.items())

print()

# 11. Delete one of the dictionary
del(dog)
try: 
    print(dog)
except NameError as e:
    print(f'Error: {e}')
    print("The dictionary does not exist. It might have been deleted.")


