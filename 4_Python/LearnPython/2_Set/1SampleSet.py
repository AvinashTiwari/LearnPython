list = [1,2,3,4,5,6,6]

print(set(list))

set1 = set([11,12,14,14,11,12])
print(set1)
print(type(set1))

set2 = {11,12,12,14,14}
print(set2)
print(type(set2))
print(len(set2))
print(11 in set2)
print(20 in set2)

set1 = {1,2,3,4,5}
set2 = {3,5,8}

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))

list1 = [1,2,3,4,5]
list2 = [3,5,8]

fs1 = frozenset(list1)
fs2 = frozenset(list2)