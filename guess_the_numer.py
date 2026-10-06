import random
def easy_level(b,chances):
    a=b
    find_number=int(input("find number: "))
    if find_number==a:
        print("you win the game! ")
    else:
        print("wrong number choosed")
        chances=chances-1
        if find_number>a:
            print("lower number required")
        elif a>find_number:
            print("higher number required")
        if chances != 0:
            easy_level(b,chances)
        else:
            print("out of chances")

def hard_level(b,chances):
    a=b
    find_number=int(input("find number: "))
    if find_number==a:
        print("you win the game! ")
    else:
        print("wrong number choosed")
        chances=chances-1
        if find_number>a:
            print("lower number required")
        elif a>find_number:
            print("higher number required")
        if chances != 0:
            easy_level(b,chances)
        else:
            print("out of chances")
def difficult_level(b,chances):
    a=b
    find_number=int(input("find number: "))
    if find_number==a:
        print("you win the game! ")
    else:
        print("wrong number choosed")
        chances=chances-1
        if find_number>a:
            print("lower number required")
        elif a>find_number:
            print("higher number required")
        if chances != 0:
            easy_level(b,chances)
        else:
            print("out of chances")


print("guess the number from 1 to 50")
choice=random.randint(1,50)
choose_level=input("choose the level 'easy' 'hard' 'difficult' ").lower()
if choose_level=="easy":
    print("you have 10 chances to find: ")
    easy_level(choice,10)
elif choose_level=="hard":
    print("you have 5 chances to find")
    hard_level(choice,5)
elif choose_level=="difficult":
    print("you have 3 chances to find")
    difficult_level(choice,3)
else:
    print("choose a valid choice")