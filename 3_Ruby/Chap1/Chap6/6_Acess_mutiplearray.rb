channels = ["A", "B","C","D"]

p channels.values_at(0)
p channels.values_at(1,2)

numbers = [0,2,3,4,5,6]

p numbers.slice(-1)
p numbers.slice(2..5)
