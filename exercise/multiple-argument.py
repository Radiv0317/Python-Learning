def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    magicnumber = kwargs.get('magicnumber', None)
    return magicnumber == 7 if magicnumber is not None else False

# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
