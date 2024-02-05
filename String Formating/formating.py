name = "John"
age = 20
print("Hello, %s!" % name)
print("%s is %d years old." % (name, age))

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

mylist = [1, 2, 3]
print("A list : %s" % mylist)

data = ("John", "Doe", 50.00)
format_string = "Hello %s %s. Your current balance is $%s"

print(format_string % data)
