# def add(*numbers):
#     c=0
#     print(numbers[0])
#     for i in numbers:
#         c+=i
#     print(c)

# add(12,34)
# add(12,32,44)
# add(23,55,66,43)

# def add(*numbers,name):
#     c=0
#     # print(name)
#     for i in numbers:
#         c+=i
#     print(c,name)

# add(12,34,name="nikhil")
# add(12,32,44,name="yuva")
# add(23,55,66,43,name="shiva")


# def info_person(*args,**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
#     print(args)

# info_person(1,2,name="nikhil",age=30,branch="cse")
# info_person(3,4,name="shyam",branch="cse")
def multiply(*numbers):
    c=1
    for i in numbers:
        c=c*i
    print(c)

multiply(12,4,-2)
multiply(2,3,-6,8)
multiply(2,5,8,9,0,6)