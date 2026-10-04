num1=int(input("enter first number: "))
operator=input("choose an operator   ' +  , - , * , / '  ")
num2=int(input("enter 2nd number: "))
result=0
to_do=False
while not to_do:
    if operator=='+':
        result=num1+num2
        print(f"{num1} + {num2} = {result}")
    elif operator=='-':
        result=num1+num2
        print(f"{num1} - {num2} = {result}")
    elif operator=='*':
        result=num1+num2
        print(f"{num1} X {num2} = {result}")
    elif operator=='/':
        result=num1+num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("choose a valid choice")
    user=input(f"if you want to continue with calculation {result} press 'y' stop type 'n' ").lower()
    if user=='y':
        to_do=False
    elif user=='n':
        to_do=True