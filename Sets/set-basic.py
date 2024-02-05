print(set("my name is michael and thats not my real name".split()))

a = set(["Jake", "John", "Mike"])
print(a)
b = set(["John", "Jill"])
print(b)

print(a.intersection(b))
print(b.intersection(a))

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(a.difference(b))
print(b.difference(a))

print(a.union(b))