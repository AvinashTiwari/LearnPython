color = "Gree1n"
if color == "Red"
   puts "Red color"
elsif color == "Green"
  puts "Greeen Color"

else
  puts "No Color found"
end


def odd_or_even(number)
  if number.odd?
    "That number is Odd"
  else
    "The Number is Even"
  end
end

p odd_or_even(10)
p odd_or_even(11)
