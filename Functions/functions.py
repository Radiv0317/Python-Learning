def my_functions():
    print("Hello From My Functions")

my_functions()

def my_functions_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

my_functions_with_args("John", "FUCK U")

def sum_two_numbers(a, b):
    return a + b

result = sum_two_numbers(3, 5)
print(result)