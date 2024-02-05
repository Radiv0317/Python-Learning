class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class")
myobjectx = MyClass()

print(myobjectx.variable)
myobjectx.function()

class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'