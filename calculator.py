from CalLogo import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

n1 = int(input("what is the first number: "))
for symbol in operations:
    print(symbol)

operations_symbol = input("pick an operation from the line above: ")
n2 = int(input("what is the second number: "))

calculation_function = operations[operations_symbol]
answer = calculation_function(n1, n2)

print(f"{n1} {operations_symbol} {n2} = {answer}")
