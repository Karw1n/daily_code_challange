import requests
from html.parser import HTMLParser

'''You are given a published Google Doc like this one (https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub) that contains a list of Unicode characters and their positions in a 2D grid. Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in the document, and prints the grid of characters. When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.

The document specifies the Unicode characters in the grid, along with the x- and y-coordinates of each character.

The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.

Any positions in the grid that do not have a specified character should be filled with a space character.

You can assume the document will always have the same format as the example document linked above.

For example, the simplified example document linked above draws out the letter 'F':

█▀▀▀
█▀▀ 
█   
Note that the coordinates (0, 0) will always correspond to the same corner of the grid as in this example, so make sure to understand in which directions the x- and y-coordinates increase.

Specifications
Your code must be written in Python (preferred), JavaScript, TypeScript, Java, Kotlin, C#, C++, Go, Rust, Swift or Ruby.

You may use external libraries.

You may write helper functions, but there should be one function that:

1. Takes in one argument, which is a string containing the URL for the Google Doc with the input data, AND

2. When called, prints the grid of characters specified by the input data, displaying a graphic of correctly oriented uppercase letters.'''

# Custom HTML parser that extracts the table data from the google doc (HTML document)
class myHTMLParser(HTMLParser):
  def __init__(self):
    super().__init__()
    self.in_table   = False
    self.in_row     = False
    self.in_cell    = False
    self.current_row  = []
    self.table        = []
    self.current_cell_data = ''
    
  def handle_starttag(self, tag, attrs):
    if tag == 'table':
      self.in_table = True
    elif tag == 'tr' and self.in_table:
      self.in_row = True
      self.current_row = []
    elif tag == 'td' and self.in_row:
      self.in_cell = True
      self.current_cell_data = ''
  
  def handle_endtag(self, tag):
    if tag == 'table':
      self.in_table = False
    elif tag == 'tr':
      if self.in_row:
        self.in_row = False
        self.table.append(self.current_row)
    elif tag == 'td':
      if self.in_cell:
        self.in_cell = False
        cleaned = self.current_cell_data.strip()
        self.current_row.append(cleaned)
  
  def handle_data(self, data):
    if self.in_cell:
      self.current_cell_data += data.strip()

# Fetches the HTML from URL and parses the table
def parse_table_from_url(url):
  response = requests.get(url)
  parser = myHTMLParser()
  parser.feed(response.text)
  return parser.table

# Convert parsed table into a dictionary
# e.g. (x, y) : character
def build_char_map(table):
  char_map = {}
  # Skip the header row
  for row in table[1:]:
      try:
        x = int(row[0])
        char = row[1]
        y = int(row[2])
        char_map[(x, y)] = char
      except (ValueError, IndexError):
        continue # In case there's a null row
  return char_map

# Render the image using character positions
def print_image(data):  
  if not data:
    print('No data to display')
    return
  
  max_x = max(x for (x, y) in data.keys())
  max_y = max(y for (x, y) in data.keys())

  for i in range(max_y + 1):
    row = ''
    for j in range(max_x + 1):
      row += data.get((j, max_y - i), ' ')
    print(row)
    
def render_character_image(url):
  table = parse_table_from_url(url)
  char_map = build_char_map(table)
  print_image(char_map)
  
render_character_image('https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub')
