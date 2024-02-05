from functools import partial

def multiply(x, y):
    return x * y

dbl = partial(multiply, 2)
print(dbl(4))

def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x
    
new_func = partial(func, 6, 6, 6)

result = new_func(6)
print(result)