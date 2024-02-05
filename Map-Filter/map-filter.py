my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(str.upper, my_pets))

# for pet in my_pets:
#     pet_ = pet.upper()
#     uppered_pets.append(pet_)

print(uppered_pets)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))

print(result)

result2 = list(map(round, circle_areas, range(1, 3)))

print(result2)



my_string = ['a', 'b', 'c', 'd', 'e']
my_number = [1, 2, 3, 4, 5]

results = list(zip(my_string, my_number))
results = list(map(lambda x, y: (x, y), my_string, my_number))

print(results)

scores = [66, 90, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75
over_75 = list(filter(is_A_student, scores))

print(over_75)

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)

from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers, 10)
print(result)


# #### Map
# from functools import reduce 

# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
# my_numbers = [4, 6, 9, 23, 5]

# map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
# filter_result = list(filter(lambda name: len(name) <= 7, my_names))
# reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

# print(map_result)
# print(filter_result)
# print(reduce_result)