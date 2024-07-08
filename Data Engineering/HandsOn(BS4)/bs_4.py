from bs4 import BeautifulSoup
import requests

r = requests.get('https://quotes.toscrape.com/')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
print(type(html))
print(type(soup))
for tag in soup.find_all('small', {'class': 'author'}):
    print(tag.string)
