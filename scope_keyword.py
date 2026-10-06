# a=10
# def display():
#     global a
#     a=a+1
#     print(a)
# display()
# print(a)


#    **** nested function***
# def display():
#     a=20
#     def show():
#         global a
#         a=a+1
#         print(a)
#     show()
# display()


def display():
    a=20
    def show():
        global a
        a=30
        print(a)
    show()
    print(a)
display()
print(a)