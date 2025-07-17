import requests
from html.parser import HTMLParser


class googleDocParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print("Ecountered a start tag: ", tag)
    
  def handle_endtag(self, tag):
    print("Encountered an end tag: ", tag)
  
  def handle_data(self, data):
    print("Encountered some data: ", data)
    
parser = googleDocParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')