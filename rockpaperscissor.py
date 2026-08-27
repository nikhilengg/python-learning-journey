import random
user_choice=int(input("enter your choice:type 0 for rock, 1 for paper , 2 for scissor : "))
computer_choice=random.randint(0,2)
print(computer_choice)
if user_choice>2:
    print("you played wrongly so try again ")
else:   

    if computer_choice==user_choice:
        print("its draw")
    elif user_choice==0 and computer_choice==2:
        print("user win")
    elif user_choice==2 and computer_choice==0:
        print("user lose")
    elif user_choice<computer_choice:
        print("user lose")
    elif user_choice>computer_choice:
        print("user win")
