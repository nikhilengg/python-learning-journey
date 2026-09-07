import math
def paint_calculation(height,width,cover):
    area=height*width
    no_of_cans=area/cover
    print(f"you will need {math.ceil(no_of_cans)} cans of paint")

h=int(input("enter height of the wall in meters: "))
w=int(input("enter width of the wall in meters: "))
coverage=7
paint_calculation(width=w,height=h,cover=coverage)