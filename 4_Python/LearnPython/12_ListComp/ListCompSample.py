list1 = []

for i in range(0,10):
    result = i ** 2
    list1.append(result)

print(list1)

list2 = [x**2 for x in range(0,10)]
print (list2)

list3 = [x**2 for x in range(0,10) if x >5]
print (list3)

set1 = {x**2 for x in range(0,10) if x >5}
print(type(set1))
print (set1)

dict1 = {x: x**2 for x in range(0,10)}
print(type(dict1))
print (dict1)


