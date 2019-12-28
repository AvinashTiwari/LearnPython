import re
mystr = "you can learn any language python2 , python3,perl, Java , javscript"

a = re.match("you", mystr)
print(a)

a = re.match("Zyys", mystr)
print(a)

a = re.match("you", mystr)
print(a.group())


a = re.match("Zyys", mystr, re.I)
print(a)

mystr = " can you learn any language python2 , python3,perl, Java , javscript"

a = re.match("Zyys", mystr, re.I)
print(a)

arp = "22.22.22.1 0 b4.g6.u7.9u VLAN:22#    L"
a = re.search(r"(.+?) + (\d) + (.+?)\s{2,}(\w)*", arp)
print(a.group(1))