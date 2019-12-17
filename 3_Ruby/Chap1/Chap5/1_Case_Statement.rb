def rate_my_food(food)
  case food
  when "milk"
    p "MILK"
  when "water"
    p "Water"
  else
    "No idea"
end
end

rate_my_food("milk")

def cal_school_grade(grade)
   case grade
     when 90..100 then "A"
     when 80..89 then "B"
     when 70..89 then "C"
     when 60..69 then "D"
       "D"
     else
       "F"
    end
  end

  p cal_school_grade(80)
