import numpy
def weekly_avg(my_cost):
    num_days = len(my_cost)
    total_cost = sum(my_cost)
    return total_cost/num_days


weekCost = [10.0,20.0,30.0]
print(weekly_avg((weekCost)))