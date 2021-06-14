from art import logo


# calculator
# Add
def add_num(n1, n2):
    return n1 + n2


# subtract
def subtract_num(n1, n2):
    return n1 - n2


# multiply
def multiply_num(n1, n2):
    return n1 * n2


# Divide
def divide_num(n1, n2):
    return n1 / n2


def exponent(n1, n2):
    return n1 ** n2


operations = {
    "+": add_num,
    "-": subtract_num,
    "*": multiply_num,
    "/": divide_num,
    "**": exponent,
}


def calculator():
    print(logo)
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation:")

        num2 = float(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer} ")
        ask = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation.: ").lower()
        if ask == 'n':
            should_continue = False
            calculator()
        elif ask == 'y':
            num1 = answer
        else:
            should_continue = False
            print("you entered a invalid input.")


calculator()
