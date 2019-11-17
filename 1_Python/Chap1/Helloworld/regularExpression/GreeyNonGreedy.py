import re
matchingRegex = re.compile(r'.at')
print(matchingRegex.findall('The fat cat sat on mat'))

nameRegex = re.compile(r'First Name: (.*)')
mo = nameRegex.findall('First Name: Avinash')
print(mo)

alligatorRegex = re.compile(r'<.*>')
mo = alligatorRegex.search('<This is> some text>')
print(mo)

nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<This is> some text')
print(mo)

regex =  re.compile(r'Banana',re.IGNORECASE)
mon = regex.search('banana')
print(mon)

agentRex = re.compile(r'Agent \w+')
print(agentRex.sub('Censored', 'Today at 5pm Agent ZYC coffe'))
