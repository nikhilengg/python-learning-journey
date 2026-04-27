piza_size=input("enter size small(s) medium(m) large(l): ")
bill=0
if piza_size=='s':
    print("small piza prise 100")
    bill+=100
elif piza_size=='m':
    print("medium piza prise 200")
    bill+=200
else:
    print("large piza prise 300")
    bill+=300
onion_pepper=input("you want pepper(y/n)")
if onion_pepper=='y':
    if piza_size=='s':
        bill+=30
    else:
        bill+=50
extra_cheese=input("you want cheese(y/n)")
if extra_cheese=='y':
    if piza_size=='s':
        bill+=50
    else:
        bill+=80
print(f"your total bill is{bill}")
print("thankyou!, have your pizza bye")