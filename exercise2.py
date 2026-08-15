import random
names=input("enter every name by separating comma ',' \n")
names_list=names.split(",")
# print(names_list)
# length=len(names_list)
# choice=random.randint(0,length-1)
# print(f"{names_list[choice]} will pay the bill")
print(f"{random.choice(names_list)} will pay the bill")