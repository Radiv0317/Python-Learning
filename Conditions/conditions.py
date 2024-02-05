x = 2 
print(x == 2)
print(x == 3)
print(x < 3)

name = "John"
age = 23
if name == "John" and age == 23 :
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick")

if name in ["John", "Rick"]:
    print("Your name is either John or Rick")

statement = False
another_statement = True
if statement is True: 
    print("is False")
    pass
elif another_statement is True:
    print("Is True")
    pass
else:
    print("FUCK U")
    pass


# IS Operator

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# NOT operator

print(not False)
print(not False) == (False)
