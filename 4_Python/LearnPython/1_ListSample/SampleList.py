list2 = [-11,2,12]
print(min(list2))
print(max(list2))

list3 = ["a","b","c"]
print(min(list3))
print(max(list3))

list3.append(list2)
print(list3)
del list3[2]
list3.pop(0)
print(list3)
print(list3.remove('b'))
print(list3.insert(0,'a'))
print(list3)
list2.extend(list3)
print(list2)
print(list2.index(-11))
list2.append(-11)
print(list2.count(-11))
list2.clear();
list2 = [-11,2,12]
print(list2.sort())
print(list2)
print(list2.reverse())
print(list2)
print(sorted(list2))
print(sorted(list2, reverse=True))
