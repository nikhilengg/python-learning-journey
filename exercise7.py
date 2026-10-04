def days_in_month(year,month):
    days_list=[31,29,31,30,31,30,31,31,30,31,30,31]
    if month==1:
        if year%4==0 and year%100!=0 or year%4==0 and year%400==0:
            print(f"february have 29 days in {year}")
        else:
            print(f"february have 28 days in{year}")
    else:
        days=days_list[month]
        print(f"{days} in a {2} month")

year=int(input("enter year: "))
month=int(input("enter a month: "))
days_in_month(year,month-1)