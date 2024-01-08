# Day 6 Assignment : Tuples
# Exercise 1 
# Create an empty tuple
empty_tuple = ()
print(empty_tuple)

# Create a tuple containing names of your sisters and your brothers
brothers = ('Waris', 'Ismail', 'Muhammad')
sisters = ('Ruqayah', 'Amina', 'Nafisat')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print("Siblings:", siblings)

# How many siblings do you have?
num_siblings = len(siblings)
print("Number of siblings:", num_siblings)

# Modify the siblings tuple and add the name of your father and mother
family_members = ('AbdulRaheem', 'Fatimah') + siblings
print("Family members:", family_members)


# Exercise 2

# Unpack siblings and parents from family_members
father, mother, *siblings = family_members
print("Father:", father)
print("Mother:", mother)
print("Remaining siblings:", siblings)

# Create fruits, vegetables, and animal products tuples
fruits = ('Apple', 'Banana', 'Orange')
vegetables = ('Carrot', 'Broccoli', 'Spinach')
animal_products = ('Eggs', 'Milk', 'Chicken')

# Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

# Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle_index] if len(food_stuff_lt) % 2 != 0 else (food_stuff_lt[middle_index - 1], food_stuff_lt[middle_index])
print("Middle item(s):", middle_item)

# Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print("First three items:", first_three_items)
print("Last three items:", last_three_items)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Is 'Estonia' a Nordic country?", 'Estonia' in nordic_countries)
print("Is 'Iceland' a Nordic country?", 'Iceland' in nordic_countries)
