import requests
from html.parser import HTMLParser


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
    
url = 'https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub'

response = requests.get(url)
html_input = response.text

parser = myHTMLParser()
parser.feed(html_input)

char_map = {}
# Skip the header row
for row in parser.table[1:]:
    try:
      x = int(row[0])
      char = row[1]
      y = int(row[2])
      char_map[(x, y)] = char
    except (ValueError, IndexError):
      continue # In case there's a null row
    
# Get the grid size
def print_image(data):  
  max_x = max(x for (x, y) in data.keys())
  max_y = max(y for (x, y) in data.keys())

  for i in range(max_y + 1):
    row = ''
    for j in range(max_x + 1):
      row += data.get((j, max_y - i), ' ')
    print(row)
    
print_image(char_map) 
