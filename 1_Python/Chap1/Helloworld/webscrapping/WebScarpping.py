import requests
from bs4 import  BeautifulSoup

data = requests.get("https://darksky.net/forecast/39.5223,-104.867/us12/en")

soup = BeautifulSoup(data.text,'html.parser')
print(soup.prettify())