import requests
from bs4 import BeautifulSoup

raw_html = requests.get('http://www.fabpedigree.com/james/mathmen.htm')
html = BeautifulSoup(raw_html.content, 'html.parser')

for i, li in enumerate(html.select('li'),start=1):
        print(i, li.text)