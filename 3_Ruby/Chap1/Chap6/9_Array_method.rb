fives = [5,10,15,20]
odds =[]
evens =[]
fives.each do |number|
  if number.even?
    evens << number
  end
  if number.odd?
    odds <<(number)
  end
end
puts odds
