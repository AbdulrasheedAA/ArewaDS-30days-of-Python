
# Approach 1: import module_name
import my_program

my_program.my_function()

# Approach 2: from module_name import function_name
from my_program import my_function

my_function()

# Approach 3: from module_name import function_name as fn
from my_program import my_function as fn

fn()

# Approach 4: import module_name as mn
import my_program as mn

mn.my_function()

# Approach 5: from module_name import *
from my_program import *

my_function()
