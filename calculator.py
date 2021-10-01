# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


mathematical_operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    is_continue = True
    number1 = float(input('What is the first number? '))

    while is_continue:
        for operation in mathematical_operations:
            print(operation)

        choose_operation = input('Pick an operation: ')
        number2 = float(input('What is the second number? '))
        answer1 = mathematical_operations[choose_operation](number1, number2)

        print(f'{number1} {choose_operation} {number2} = {answer1}')
        is_continue = input('Do you want to continue? Type y/n: ').lower()

        if is_continue == 'y':
            number1 = answer1
            is_continue = True
        else:
            is_continue = False
            calculator()


calculator()
