from art import logo

print(logo)


# add function
def add(first_number, second_number):
    return first_number + second_number


# Subtract function
def subtract(first_number, second_number):
    return first_number - second_number


# Divide function
def divide(first_number, second_number):
    return first_number / second_number


# Multiply function
def multiply(first_number, second_number):
    return first_number * second_number

# fonksiyonları listeledğimiz bir dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

is_finished = False

while not is_finished:
    first_number = int(input("Give us the first number : "))
    second_number = int(input("Give us the second number : "))
    for symbol in operations:
        print(symbol)
    operation = input("Select the operation above : ")
    function = operations[operation]
    answer = function(first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {answer}")
    wish = input("Do you want to make another calculation : (Y) or (N) ").lower()
    if wish == "n":
        is_finished = True