# __Author__ __Lencof__
# downloader.py

from bs4 import BeautifulSoup
import requests
from requests import get


page = requests.get(input('your URL'))
filetype = '.' + input('Enter File Extension (with no dot): ')
soup = BeautifulSoup(page.text, 'html.parser')
