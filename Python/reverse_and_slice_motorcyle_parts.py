# Coddy.tech Daily Challenge 12/06/2025
# Coddy.tech DC 12/06/2025
'''Create a function named organize_parts that receives parts_list, start_index, and end_index as its parameters.

As a vintage motorcycle enthusiast, you need to organize your collection of motorcycle parts. Your task is to reverse the order of parts and then select a specific range from the reversed list.

The function should perform the following steps:

Reverse the entire string of parts.
Split the reversed string into a list of individual parts.
Return a slice of the reversed list based on the given start and end indices.
Parameters:

parts_list (str): A string of motorcycle parts separated by commas.
start_index (int): The starting index for slicing (inclusive).
end_index (int): The ending index for slicing (exclusive).
The function returns a list of strings representing the selected range of parts from the reversed list.'''

parts_list, start, end = 'carburetor,piston,spark plug,clutch,brake pad', 0, 2

# So function takes in a list, and two indexs (start and end), and we want to modify the list and return a slice of the list as stated by the start and indexes
# def organize_parts(parts_list, start_index, end_index):
#   pass

# What I am going to do first is create the functionality to perform steps 1 to 3, and once they all work I'll put it together in a function.

# 1. Reverse the entire string of parts. My approach is to use slicing iteration [::-1]
# reversed_parts_string = parts_list[::-1]
# print(reversed_parts_string) # dap ekarb,hctulc,gulp kraps,notsip,roterubrac

# 2. Split the reversed string into a list of individual parts.
# Upon reading this requirement I realised that the input is not a list but a string and therefore need to go back and remodify the functionality to accomadate strings not lists.
# reversed_parts_list = reversed_parts_string.split(',')
# print(reversed_parts_list) # ['dap ekarb', 'hctulc', 'gulp kraps', 'notsip', 'roterubrac']

# 3. Return a slice of the reversed list based on the given start and end indices.
# Using slicing I shall return the wanted sliced section
# final_list = reversed_parts_list[start:end]
# print(final_list)

# Now that each functionality has been tried and tested I shall put it together into one function
def organize_parts(parts_list, start_index, end_index):
    # 1. Reverse the entire string of parts 
    reversed_parts_string = parts_list[::-1] 
    # 2. Split the reversed string into a list of individual parts.
    reversed_parts_list = reversed_parts_string.split(',')
    # 3. Return a slice of the reversed list based on the given start and end indices.
    return reversed_parts_list[start_index:end_index]
  
print(organize_parts(parts_list, start, end)) # ['dap ekarb', 'hctulc']
# Success. As it is a relatively basic challenge I did not have to account for any edge cases.
