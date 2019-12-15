def meal_plan(time_of_week, time_day)
  if time_of_week == "weekday"
    if time_day == "breakfast"
      p "Cereal"
    elsif time_day == "lunch"
      p "Sandwich"
    elsif time_day == "dinner"
      p "dinner"
    end

  elsif time_of_week == "weekend"
    if time_day == "breakfast"
      p "French Toast"
    elsif time_day == "lunch"
      p  "Pizza"
    elsif time_day == "dinner"
      p "weekend dinner"
    end

  end

end


meal_plan("weekday", "breakfast")
