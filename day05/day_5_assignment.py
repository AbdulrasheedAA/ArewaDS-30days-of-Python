# Exercise 1

# Declare an empty list
empty_list = []
print(empty_list)

# Declare a list with more than 5 items
list_with_items = [1, 'apple', True, 3.14, ['nested', 'list'], {'key': 'value'}]
print(list_with_items)

# Find the length of your list
list_length = len(list_with_items)
print(list_length)

# Get the first item, the middle item, and the last item of the list
first_item = list_with_items[0]
middle_item = list_with_items[len(list_with_items) // 2]
last_item = list_with_items[-1]
print(first_item, middle_item, last_item)

# Declare a list called mixed_data_types
mixed_data_types = ['YourName', 25, 1.75, 'Single', 'YourAddress']
print(mixed_data_types)

# Declare a list variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list
print(it_companies)

# Print the number of companies in the list
num_companies = len(it_companies)
print(num_companies)

# Print the first, middle, and last company
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[2] = 'Microsoft Updated'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('NewCompany')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'InsertedCompany')

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4] = it_companies[4].upper()
print(it_companies)

# Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)
print(joined_companies)

# Check if a certain company exists in the it_companies list
company_to_check = 'Google'
if company_to_check in it_companies:
    print(f'{company_to_check} exists in the list.')
else:
    print(f'{company_to_check} does not exist in the list.')

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print(first_three_companies)

# Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print(last_three_companies)

# Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
middle_company = it_companies[middle_index] if num_companies % 2 != 0 else it_companies[middle_index - 1:middle_index + 1]
print(middle_company)

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(middle_index) if num_companies % 2 != 0 else it_companies.pop(middle_index - 1)
print(it_companies)
# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
full_stack_in = full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack_in = full_stack.insert(full_stack.index('Redux')+2, 'SQL')
print(full_stack)
print(full_stack_in)


# Exercise 2


# The following is a list of 10 students ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
min_age = min(ages)
max_age = max(ages)

# Add the min age and max age again to the list
ages.extend([min_age, max_age])
print(ages)
# Find the median age
sorted_ages = sorted(ages)
median_age = (sorted_ages[len(sorted_ages) // 2 - 1] + sorted_ages[len(sorted_ages) // 2]) / 2

# Find the average age
average_age = sum(ages) / len(ages)

# Find the range of the ages
age_range = max_age - min_age

# Compare the value of (min - average) and (max - average), use abs() method
min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)

print(f"min_age: {min_age}", 
      f"max_age: {max_age}", 
      f"median_age: {median_age}", 
      f"average_age: {average_age}", 
      f"age_range: {age_range}", 
      f"min_average_diff: {min_average_diff}", 
      f"max_average_diff: {max_average_diff}"
)


# Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
middle_countries = countries[len(countries) // 2 - 1:len(countries) // 2 + 1] if len(countries) % 2 == 0 else countries[len(countries) // 2]

# Divide the countries list into two equal lists if it is even if not one more country for the first half
half_length = len(countries) // 2
first_half_countries = countries[:half_length] if len(countries) % 2 == 0 else countries[:half_length + 1]
second_half_countries = countries[half_length:]

# Unpack the first three countries and the rest as scandic countries
# Countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first_country, second_country, third_country, *scandic_countries = countries

print("First three countries:", first_country, second_country, third_country)
print("Scandic countries:", scandic_countries)