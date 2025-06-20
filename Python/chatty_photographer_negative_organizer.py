# Daily Coding Challenge Chatty Photographer's Negative Organizer
# Coddy.tech DC 20/06/2025

# Function that returns the roll number 
def get_roll_num(roll):
  return int(roll.rsplit(' ')[0]) # rsplit used to seperate string by whitespace and the [0] is the first item
  # .split() would have done the same thing

def organize_negatives(negatives : list):
  # Sort the negatives by the roll number
  negatives.sort(key=get_roll_num)
  # Join the items using '\n'
  return '\n'.join(negatives)
  
negatives = ["2 Beach sunrise", "1 Mountain view", "3 City lights"]
print(organize_negatives(negatives))
  
'''Create a function named organize_negatives that receives negatives as its parameter.

You are a chatty photographer organizing your collection of photographic negatives in a darkroom. To keep things tidy, you want to sort the negatives by their film roll number and format the results for your records.

Your task is to implement a function that:

Sorts the negatives by their film roll number (in ascending order).
Formats the sorted negatives into a single string, with each entry separated by a newline character "\n".
Parameters:

negatives (list of str): A list of strings. Each string is in the format "roll_number description", where roll_number is a positive integer and description contains only spaces and alphabetic characters.
The function returns a string containing the sorted negatives, with each entry on a new line.

Example:


# Example usage:
negatives = ["2 Beach sunrise", "1 Mountain view", "3 City lights"]
result = organize_negatives(negatives)
print(result)
# Output:
# 1 Mountain view
# 2 Beach sunrise
# 3 City lights
Note:

Make sure the sorting is stable (if two negatives have the same roll number, their original order should be maintained).
You can assume that the input list will not be empty.'''

# Coddy.Tech solution
# def organize_negatives(negatives):
#     # Sort the negatives based on the roll number
#     sorted_negatives = sorted(negatives, key=lambda x: int(x.split()[0]))
    
#     # Join the sorted negatives with newline characters
#     return "\n".join(sorted_negatives)