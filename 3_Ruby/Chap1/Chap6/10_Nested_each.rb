shirts = ["strip", "plain white", "plaid", "band"]
ties = ["dot", "color", "borning"]
shirts.each do |shirt|
  ties.each do |tie|
    puts "Options #{shirt} for tie #{tie}"
  end
end
