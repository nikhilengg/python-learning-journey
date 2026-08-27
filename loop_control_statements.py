# break statement
# list1=['hi','hello','welcome']
# names=['krishn','ram','madhav']
# for item in list1:
#     for name in names:
#         print(item,name)
#         if item=='hello' and name=='ram':
#             break
#     print("out from inner loop")
# print("out from outer loop")

# continue statement
count=0
while count<10:
    print(count)
    count+=1
    if count==7:
        continue
    print("hi")