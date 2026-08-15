# tuple1=(12,6,-8,'nikhil',True)
# # print(tuple1)
# # print(tuple1[2])
# # print(tuple1[-2])
# # print(tuple1[1:3:1])
# print(type(tuple1))
# #tuples are immutable 
# #tuple1[2]=6
tuple1=(12,6,-8,'nikhil',True,12)
tuple2=(3,6,1,'nikhil','bob')
# tuple3=(tuple1,tuple2)
tuple3=tuple1+tuple2 #concatination
print(tuple3)
# print(min(tuple1)) #mix kind of tupple cannot possible to find min and max values
print(tuple1.count(12)) #count to repeated item in a tupple