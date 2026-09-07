# # # positional arguments
# # def greet(name,dept):
# #     print(f"hi{name}")
# #     print(f"are you from {dept} department")

# # greet("nikhil","cs")


# # keyword arguments
# # def greet(name,subject,dept):
# def greet(name,subject,dept="cs"):
#     print(f"hi {name}")
#     print(f"do you teach{subject}")
#     print(f"are you from {dept} department")


# # greet(dept="cs",name="nikhil")
# # greet("ramu","python",dept="cse")
# greet("nikhil","python","eee")

def add(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(f"sum is{c}")

add(5,7,9)
add(4,3,2,5,7,8,9,34,21,44,4,4,3,4,5,6,66666,321,43)
