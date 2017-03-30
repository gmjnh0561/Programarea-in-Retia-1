from urllib.request import urlopen
from bs4 import BeautifulSoup as BS4

url = urlopen('http://ferestremd.md')
bsObj = BS(url, 'lxml')

title = bsObj.title.get_text()

print("Title of the website is: {}".format(title))


