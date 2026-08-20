# tuple1=(2,56,34,3,5,-1)
# for i in tuple1:
#     print(i)
#     if i==5:
#         break
# else:
#     print("loop successfully completed and we are in else block now!!!")
tuple1=(2,56,34,3,5,-1)
for i in tuple1:
    if i%6==0:
        print(i)
        break
else:
    print("there is no number divisible by 6 in this sequence")
