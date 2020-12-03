from art import logo

print(logo)


def operation(first_number, second_number, operation):
    if operation == "/":
        return first_number / second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    else:
        return "Invalid operation"


is_finished = False
while not is_finished:
    first_number = int(input("First number : "))
    myoperation = input("""Select the operation below : 
    + 
    -
    *
    /
    """)
    second_number = int(input("Second number : "))
    sonuc = operation(first_number, second_number, myoperation)
    print(f"The output is {sonuc}")
    is_finished_input = input("Do you want to contunie Y or N : ").lower()
    if is_finished_input == "n":
        is_finished = True
