# Task 1 - Concatenate strings
concatenated_str1 = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
print(concatenated_str1)

# Task 2 - Concatenate strings
concatenated_str2 = ' '.join(['Coding', 'For', 'All'])
print(concatenated_str2)

# Task 3 - Declare a variable
company = "Coding For All"

# Task 4 - Print the variable
print(company)

# Task 5 - Print the length of the company string
print(len(company))

# Task 6 to 8 - Uppercase, lowercase, and formatting
uppercase_company = company.upper()
lowercase_company = company.lower()
capitalize_company = company.capitalize()
title_company = company.title()
swapcase_company = company.swapcase()

print(uppercase_company)
print(lowercase_company)
print(capitalize_company)
print(title_company)
print(swapcase_company)

# Task 9 - Cut out the first word
cut_first_word = company.split()[0]
print(cut_first_word)

# Task 10 - Check if the string contains a word


# Task 11 - Replace word
replaced_company = company.replace('Coding', 'Python')
print(replaced_company)

# Task 12 - Replace word
replaced_python = replaced_company.replace("All", "Everyone")
print(replaced_python)

# Task 13 - Split the string
split_company = company.split()
print(split_company)

# Task 14 - Split string at commas
comma_separated = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', ')
print(comma_separated)

# Task 15 - Character at index 0
char_at_index_0 = company[0]
print(char_at_index_0)

# Task 16 - Character at Last index
last_index = len(company) - 1
print(last_index)

# Task 17 - Character at index 10
char_at_index_10 = company[10]
print(char_at_index_10)


# Task 18 to 19 - Acronym
acronym_python_for_everyone = ''.join(word[0] for word in "Python For Everyone".split())
acronym_coding_for_all = ''.join(word[0] for word in "Coding For All".split())
print(acronym_python_for_everyone)
print(acronym_coding_for_all)

# Task 20 to 22 - Index and find
position_C = company.index('C')
position_F = company.index('F')
last_l = company.rfind('l')

print(position_C)
print(position_F)
print(last_l)

# 23 - Index or find for 'because'
position_because = 'You cannot end a sentence with because because because is a conjunction'.find('because')
print(position_because)

# 24 - rindex for 'because'
last_position_because = 'You cannot end a sentence with because because because is a conjunction'.rindex('because')
print(last_position_because)

# 25 - Slice out phrase
because_phrase = 'You cannot end a sentence with because because because is a conjunction'[position_because:position_because + len('because because because')]
print(because_phrase)

# String starts with and ends with
starts_with_coding = company.startswith('Coding')
ends_with_coding = company.endswith('coding')
print(starts_with_coding)
print(ends_with_coding)


# Remove trailing spaces
trimmed_company = '   Coding For All      '.strip()
print(trimmed_company)

# isidentifier
is_identifier_1 = '30DaysOfPython'.isidentifier()
is_identifier_2 = 'thirty_days_of_python'.isidentifier()
print(is_identifier_1)
print(is_identifier_2)


# Join list with a hash with space string
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(python_libraries)
print(joined_libraries)


# New line escape sequence
new_line_escape = 'I am enjoying this challenge.\nI just wonder what is next.'
print(new_line_escape)


# Tab escape sequence
tab_escape = 'Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'
print(tab_escape)


# String formatting
radius = 10
area = 3.14 * radius ** 2
formatted_area = f'The area of a circle with radius {radius} is {area} meters square.'
print(formatted_area)

# String formatting for mathematical operations
result_add = f'8 + 6 = {8 + 6}' 
result_subtract = f'8 - 6 = {8 - 6}'
result_multiply = f'8 * 6 = {8 * 6}'
result_divide = f'8 / 6 = {8 / 6:.2f}'
result_modulo = f'8 % 6 = {8 % 6}'
result_floor_divide = f'8 // 6 = {8 // 6}'
result_power = f'8 ** 6 = {8 ** 6}'

print(result_add)
print(result_subtract)
print(result_multiply)
print(result_divide)
print(result_modulo)
print(result_floor_divide)
print(result_power)