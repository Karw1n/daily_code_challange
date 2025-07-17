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
    
      
html_input = '<table class="c5"><tbody><tr class="c2"><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">x-coordinate</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">Character</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">y-coordinate</span></p></td></tr><tr class="c2"><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">0</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">█</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">0</span></p></td></tr><tr class="c2"><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">0</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">█</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">1</span></p></td></tr><tr class="c2"><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">0</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">█</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">2</span></p></td></tr><tr class="c2"><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">1</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">▀</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">1</span></p></td></tr><tr class="c2"><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">1</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">▀</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">2</span></p></td></tr><tr class="c2"><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">2</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">▀</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">1</span></p></td></tr><tr class="c2"><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">2</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">▀</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">2</span></p></td></tr><tr class="c2"><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">3</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">▀</span></p></td><td class="c1" colspan="1" rowspan="1"><p class="c4"><span class="c0">2</span></p></td></tr></tbody></table>'

parser = myHTMLParser()
parser.feed(html_input)

# Print results
for row in parser.table:
    print(row)
