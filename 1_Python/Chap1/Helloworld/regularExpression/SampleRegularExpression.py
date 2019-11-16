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

phoneNumerRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneNumerRegex.search("this my number 123-456-7890")
print(mo)
mo = phoneNumerRegex.search("this my number 456-7890")
print(mo)

batRegex = re.compile(r'Bat(wo)*man')
bat = batRegex.search("I am Batwoman")
print(bat)
bat = batRegex.search("I am Batwowowowoman")
print(bat)
bat = batRegex.search("I am Batman")
print(bat)

batRegex = re.compile(r'Bat(wo)+man')
bat = batRegex.search("I am Batwoman")

phoneNumerRegex = re.compile(r'\D\D\D')
mo = phoneNumerRegex.search('123 asd')
print(mo)

phoneNumerRegex = re.compile(r'\w\w\w')
mo = phoneNumerRegex.search('asd')
print(mo)

phoneNumerRegex = re.compile(r'\W\W\W')
mo = phoneNumerRegex.search('asd***')
print(mo)

phoneNumerRegex = re.compile(r'\s\w+')
mo = phoneNumerRegex.search(' asd***')
print(mo)

phoneNumerRegex = re.compile(r'\d+\s\w+')
mo = phoneNumerRegex.findall('12 peechs 14 lemon 15 cherries')
print(mo)

vowl = re.compile(r'[AEIOUaeiou]')
vo = vowl.findall('This is a sentence vowl')
print(vo)

vowl = re.compile(r'[^AEIOUaeiou]')
vo = vowl.findall('This is a sentence vowl')
print(vo)

beginning = re.compile(r'^Hello')
vo = beginning.findall('Hello Avinash')
print(vo)

beginning = re.compile(r'\d+$')
vo = beginning.findall('Avinash 1221')
print(vo)