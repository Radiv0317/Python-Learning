def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)   
    return data_transmitter


func2 = transmit_to_space("Burn the Sun!")
func2()

def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)

print_msg(9)


def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))