colors = ["Red", "Blue", "Green","Yellow"]
colors.each do |color , index|
  puts color
  puts index
end

colors.each_with_index do |color , index|
  puts color
  puts index
end
