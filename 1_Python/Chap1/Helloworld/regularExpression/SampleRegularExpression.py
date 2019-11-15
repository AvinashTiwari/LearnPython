import re

str = "my phone is 425-342-2222"

phoneNumerRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
monumber = phoneNumerRegex.search(str)
print(monumber.group())
print(monumber.group(1))
print(monumber.group(2))

Sentence = "I love fruits , I all love sort of berries , i am fan of strawberries, blueberries"

fruitRegex = re.compile(r'strawberries|blueberries')
fruit = fruitRegex.search(Sentence)
print(fruit.group())
