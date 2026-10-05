# a=15 #global scope
# def display():
#     a=10 #local scope
#     print(a)
# display()
# print(a)

a=15 #global scope
def display():
    a=10 #local scope
    # print(a)
    def show():
        print(a)
display()