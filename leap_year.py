"""
year=int(input("enter year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"leap year{year}")
        else:
            print("not leap year")
    else:
        print(f"leap year {year}")
else:
    print("not a leap year")

"""
year=int(input("enter year: "))
if(year%4==0 and year%100!=0 or year%400==0):
    print(f"{year} leap year")
else:
    print(f"{year} not leap year")
    