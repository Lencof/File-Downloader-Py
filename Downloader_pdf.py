import urllib
import requests

url = 'https://workspace.google.com//en/googleblogs/pdfs/google_predicting_the_present.pdf' # random project pdf file
urllib.urlretrieve(url, "test2.pdf")
r = requests.get(url)

with open("test2.pdf", "wb") as code:
    code.write(r.content)
