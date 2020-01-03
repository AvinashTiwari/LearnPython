class Gadget
end
phone =  Gadget.new
laptop = Gadget.new
microwave = Gadget.new

p String.new("Avinash")
puts phone
puts laptop
puts microwave

puts Gadget.superclass
puts Gadget.superclass.superclass

puts phone.is_a?(Gadget)
#puts phone.methods.sort
