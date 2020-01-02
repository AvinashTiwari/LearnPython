def my_dec(target_funtion):
    def function_wrapper():
        return " Target Function is " + target_funtion() + " is called"
    return  function_wrapper()

@my_dec
def target_function():
    return  "cool"

print(target_function)