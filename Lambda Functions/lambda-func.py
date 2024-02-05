def sum(a, b):
    return a + b

a = 1
b = 2 
c = sum(a,b)
print(c)

sum = lambda x,y : x+y
print(c)


l = [2, 4, 7, 3, 14, 19]

for i in l:
    print((lambda x: "True" if x % 2 != 0 else "False")(i))