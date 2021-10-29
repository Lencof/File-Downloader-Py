# __Author__ __Lencof__
# downloader.py

from bs4 import BeautifulSoup
import requests
from requests import get
from README import README

DW = '''
     __Author__ __Lencof__
     # downloader.py
     '''

print(DW)

page = requests.get(input('URL'))
filetype = '.' + input('Enter File Extension (with no dot): ')
soup = BeautifulSoup(page.text, 'html.parser')

for link in soup.find_all('a'):
    url = link.get('href')
    if filetype in url:
        print(url)
        with open(url, 'wb') as file:
            response = get(url)
            file.write(response.content)
        else:
          print(' None, not connected ')
