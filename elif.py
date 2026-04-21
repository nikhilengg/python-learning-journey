height=float(input("enter height in feet: "))
if height>=3:
    print("eligible for ride")
    age=int(input("enter age"))
    if age<=12:
        print("pay 150")
    elif age<=18:
        print("pay 250")
    else:
        print("pay 500")
else:
    print("not eligible for ride")
print("bye")