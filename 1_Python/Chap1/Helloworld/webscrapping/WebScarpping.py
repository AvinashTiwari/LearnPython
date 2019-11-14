import requests
from bs4 import  BeautifulSoup

data = requests.get("https://darksky.net/forecast/39.5223,-104.867/us12/en")

soup = BeautifulSoup(data.text,'html.parser')
print(soup.prettify())
#print(soup.head())
#print(soup.body())
#print(soup.title)
paragraph = soup.body.div
print(type(paragraph))
print(paragraph.text)
print(paragraph['class'])
print(paragraph.attrs)

for string in soup.strings:
    print(string)

for string in soup.stripped_strings:
    print(string)

print("Avinash " + soup.body.next_sibling)

sapn = soup.select('span.temp')
print(sapn)
print(sapn[0])