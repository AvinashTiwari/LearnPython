a =  lambda x,y : x*y
print(type(a))
print(a(10,50))

b = lambda  mylist: [x*y for x in range(10) for y in range(5)] +mylist

print(b([10,100,100]))