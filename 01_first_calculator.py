from art import logo

print(logo)


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


is_finished = False
while not is_finished:
    first_number = int(input("First number : "))
    operation = input("""Select the operation below : 
    + 
    -
    *
    /
    """)
    second_number = int(input("Second number : "))

    if operation == "/":
        print(divide(first_number, second_number))
    elif operation == "*":
        print(multiply(first_number, second_number))
    elif operation == "+":
        print(sum(first_number, second_number))
    elif operation == "/":
        print(sub(first_number, second_number))
    else:
        print("Invalid operation")
    is_finished_input = input("Do you want to contunie Y or N : ").lower()
    if is_finished_input == "n":
        is_finished=True