import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here
    salaries_dict = json.loads(salaries_json)
    salaries_dict[name] = salary
    new_salaries_json = json.dumps(salaries_dict)
    return new_salaries_json

# Test code
salaries = '{"Alfred": 300, "Jane": 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])