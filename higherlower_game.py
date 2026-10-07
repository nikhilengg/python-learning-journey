import random
import game_database
print("LOWER HIGHER")
score=0

def display_accountinfo(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f" {name}, a {description}, from {country}"

def check_answer(guess,follower_1,follower_2):
    if follower_1<follower_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False

continue_flag=True
while continue_flag:
    account_1=random.choice(game_database.data)
    account_2=random.choice(game_database.data)
    print(f"compare 1: {display_accountinfo(account_1)}")

    print("VS")

    print(f"compare 2: {display_accountinfo(account_2)}")

    guess=int(input("who has more followers 1 or 2:  "))
    follower_count_1=account_1["follower_count"]
    follower_count_2=account_2["follower_count"]
    print(follower_count_1)
    print(follower_count_2)
    is_correct=(check_answer(guess,follower_count_1,follower_count_1))
    if is_correct:
        score=score+1
        print(f"you are right. your score is{score} ")

    else:
        print(f"you are wrong.. your final score is: {score}")
        continue_flag=False

