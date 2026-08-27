import random 
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','%','^','&','*','(',')','-','+']
print("welcome to password generator")
# list1=[letters,numbers,symbols]
n_letters=int(input("how many letters you want in your password: "))
n_numbers=int(input("how many numbers you want in your password: "))
n_symbols=int(input("how many symbols you want in your password: "))

password_list=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list.append(char)
# print(password)
for i in range(1,n_numbers+1):
    num=random.choice(numbers)
    password_list.append(num)
for i in range(1,n_symbols+1):
    symb=random.choice(symbols)
    password_list.append(symb)
random.shuffle(password_list)
print(password_list)
print("".join(password_list))