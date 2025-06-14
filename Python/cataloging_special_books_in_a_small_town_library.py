# Cataloging Special Books in a Small Town Library
# Coddy.tech DC 14/06/2025

# First I shall define the structure of the function.
# Using the parameters book_ages (list of int) and special_year we return all the books that are older than the special year (int)

'''Requirements:
- Use a for loop to iterate through
- Use continue statement to skip books that are not older than the special year
- Use the break statement to stop counting if a book is older than 200 years
- Use increment operators to keep track of the count and the current book being examined
'''

def count_special_books(book_ages, special_year):
  count = 0
  # For loop to iterate through the list
  for i in range(0, len(book_ages)):
    # Stop if book older than 200
    if book_ages[i] > 200:
      break
    # Carry on if book is not older than special_year
    elif (book_ages[i]) <= special_year:
      continue
    # Otherwise book is older than special_year and not older than 200 so ammend count by 1
    else:
      count += 1
  return count

'''Create a function named count_special_books that receives book_ages and special_year as its parameters.

Your task is to count the number of books that are older than the special year, but stop counting if you encounter a very old book (over 200 years old).

Implement this function to simulate cataloging books in a small town library on a quiet afternoon.

Parameters:

book_ages (list of int): A list of integers representing the ages of books in years.
special_year (int): An integer representing a significant year in the town's history.
The function should return an integer representing the count of special books.

Requirements:

Use a for loop to iterate through the book_ages list.
Use the continue statement to skip books that are not older than the special_year.
Use the break statement to stop counting if a book older than 200 years is encountered.
Use increment operators to keep track of the count and the current book being examined.'''

# Their solution.
# def count_special_books(book_ages, special_year):
#     count = 0
#     for age in book_ages:
#         if age <= special_year:
#             continue
#         if age > 200:
#             break
#         count += 1
#     return count