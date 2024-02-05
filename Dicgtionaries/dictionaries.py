phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

phonebook = {"John": 133333, "Jack" : 2392180, "Jill" : 91203980}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
