def my_first_function():
    "This first function"
    print("hello")

help(my_first_function())


def my_first_function_arg(x,y,z):
    sum_xyz = (x+y)*z
    return sum_xyz

print(my_first_function_arg(x=1,y=2,z=3))

def function1(x, *args):
    print(x)
    for argument in args:
        print(argument)

print(function1(1,2,3))