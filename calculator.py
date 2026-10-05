import os

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
operation_dict={
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}

def calculator():
    number1=float(input("enter 1st number: "))
    for symbol in operation_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        operator=input("pick an operator: ")
        number2=float(input("enter 2nd number: "))
        calculator_function=operation_dict[operator]
        output=calculator_function(number1,number2)
        print(f"{number1} {operator} {number2} = {output}")
        should_continue=input(f"enter y to continue with {output} or n to new calculation or x to exit").lower()
        if should_continue=='y':
            number1=output
            continue_flag=True
        elif should_continue=='n':
            os.system("cls")
            continue_flag=False
            calculator()
        else:
            continue_flag=False
            print("bye dengey")

calculator()