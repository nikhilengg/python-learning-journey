a=input("enter numbers seperating by space: ")
numbers_list=a.split()
# print(numbers_list)
count=0
for i in numbers_list:
    count=count+1
# 2print(count)
for i in range(0,count):
    numbers_list[i]=int(numbers_list[i])
# print(numbers_list)
max1=numbers_list[0]
for i in range(1,count):
    if max1<numbers_list[i]:
        max1=numbers_list[i]
print(max1)
print(max(numbers_list))