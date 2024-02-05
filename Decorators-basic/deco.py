# @decorator
# def function(arg):
#     return "value"
# function = decorator(function)

def repeater(old_function):
    def new_function(*args, **kwds):
        old_function(*args, **kwds)
        old_function(*args, **kwds)
    return new_function
@repeater

def multiply(num1, num2):
    print(num1 * num2) 
multiply(2, 3)

def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds)
    return new_function

def double_Ii(old_function):
    def new_function(arg):
        return old_function(arg * 2)
    return new_function

def check(old_function):
    def new_function(arg):
        if arg < 0: raise (ValueError, "Negative Argument")
        old_function(arg)
    return new_function

def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator

@multiply(3)
def return_num(num):
    return num
return_num(5)