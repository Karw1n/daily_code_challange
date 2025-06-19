# Daily Coding Challenge Botanical Cell Size Analyzer
# Coddy.tech DC 19/06/2025

# I was required to sort the input array without using the built in sort() method    
# Insertion Sort O(n^2)   
def sort_list(lst : list):
  sorted_list = []
  
  for i in range(len(lst)):
    if len(sorted_list) == 0:
      sorted_list.append(lst[i])
    else:
      iter = 0
      added = False
      while iter < len(sorted_list) and not added:
        if lst[i] < sorted_list[iter]:
          sorted_list.insert(iter, lst[i])
          added = True
        iter += 1
      if not added:
        sorted_list.append(lst[i])
  return sorted_list
print(sort_list([2, 1, 5, 10, 11, 4, 8, 23]))


def analyze_plant_samples(samples):
  samples = sort_list(samples)
  small = medium = large = xl = 0
  for i in range(len(samples)):
    if samples[i] >= 1 and samples[i] <= 5:
      small += 1
    elif samples[i] >= 6 and samples[i] <= 10:
      medium += 1
    elif samples[i] >= 11 and samples[i] <= 15:
      large += 1
    else:
      xl += 1
  final_string = f'Small: {small}, Medium: {medium}, Large: {large}, Extra-large: {xl}'
  return final_string

# Reflection: I felt like this could have been compelted using a dictionary and addiotionaly the sorting seemed a bit redudant.
'''
Create a function named analyze_plant_samples that receives samples as its parameter.

You are a scientist in a botanical research lab examining plant samples under a microscope. Your task is to analyze the sizes of plant cells and categorize them.

The function should sort the samples from smallest to largest, then count how many samples fall into specific size categories.

Parameters:

samples (list of int): An array of integers representing plant cell sizes in micrometers.
The function returns a string summarizing the findings in this format: "Small: X, Medium: Y, Large: Z, Extra-large: W" where X, Y, Z, and W are the counts of samples in each category.

Follow these steps:

Sort the input array in ascending order using a basic sorting algorithm (do not use built-in sort functions).
Count the samples in each category:
Small cells: 1-5 micrometers
Medium cells: 6-10 micrometers
Large cells: 11-15 micrometers
Extra-large cells: 16 micrometers and above
Return the formatted string with the counts.
'''

# Provided Solution
# def analyze_plant_samples(samples):
#     # Step 1: Sort the input array using bubble sort
#     n = len(samples)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if samples[j] > samples[j + 1]:
#                 samples[j], samples[j + 1] = samples[j + 1], samples[j]

#     # Step 2: Count the samples in each category
#     small = medium = large = extra_large = 0

#     for size in samples:
#         if 1 <= size <= 5:
#             small += 1
#         elif 6 <= size <= 10:
#             medium += 1
#         elif 11 <= size <= 15:
#             large += 1
#         else:
#             extra_large += 1

#     # Step 3: Return the formatted string
#     return f"Small: {small}, Medium: {medium}, Large: {large}, Extra-large: {extra_large}"