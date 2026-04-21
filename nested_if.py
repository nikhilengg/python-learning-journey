height=int(input("enter height: "))
if height>3:
    print("eligible for ride")
    age=int(input("enter age"))
    if age<=18:
        print("pay 250rs")
    else:
        print("pay 500rs")
else:
    print("not eligible for ride")
    