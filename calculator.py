
#define all operation functions

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


def calculator():
    num1 = float(input("What's the First Number?: "))

    #print all possible operations
    operations = {"+" : add, "-": subtract, "*": multiply, "/": divide }
    for key in operations:
        print(key)

    operation_symbol = input("pick an operation from the line above: ")
    num2 = float(input("what's the second number?: "))


    first_result = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {first_result}")


    to_cont = input(f"type 'y' to continue calculating with {first_result}, or type 'n' to exit: ").lower()
    if to_cont == "n":
        continue_calc = False 

    if to_cont == "y":
        continue_calc = True

    #loop operation if user wants to continue opertation
    while continue_calc:
        operation_symbol = input("pick another operation: ")
        num3 = float(input("What's the next number?: "))
        second_result = operations[operation_symbol](first_result, num3)
        print(f"{first_result} {operation_symbol} {num3} = {second_result}")
        first_result = second_result
        to_cont = input(f"type 'y' to continue calculating with {second_result}, or type 'n' to start a new calculation ")
        if to_cont == "n":
            continue_calc = False
            calculator()
        
        
calculator()