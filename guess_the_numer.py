import random


print("guess the number from 1 to 50")
choice=random.randint(1,50)
choose_level=input("choose the level 'easy' 'hard' 'difficult' ")
if choose_level=="easy":
    print("you have 10 chances to find: ")