#Arithmetic Operators
# Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.
number = 1 + 2 * 3 / 4.0
print(number)


# Try to predict what the answer will be. Does python follow order of operations?

# Another operator available is the modulo (%) operator, which returns the integer remainder of the division. dividend % divisor = remainder.
remainder = 11 % 3
print(remainder)

# Using two multiplication symbols makes a power relationship.
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# Using Operators with Strings
helloworld = "hello" + " " + "world"
print(helloworld)

# Python also supports multiplying strings to form a string with a repeating sequence:
lotofhello = "hello" * 10
print(lotofhello)

# Using Operators with Lists
# Lists can be joined with the addition operators:
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:
print([1, 2, 3] * 3)

x = (20)
y = (40)

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")