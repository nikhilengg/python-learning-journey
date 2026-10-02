import os

def find_winner(bidders_details):
    highest_bid=0
    winner=""
    for bidder in bidders_details:
        bidding_price=bidders_details[bidder]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"highest bid winner is {winner}")




bidders_data={} 
end_of_bidders=False
while not end_of_bidders:
    name=input("enter name: ")
    price=int(input("enter your bid amount: "))
    bidders_data[name]=price
    more_bidders=input("are there more bidders? type yes or no : ").lower()
    if more_bidders=='no':
        end_of_bidders=True
        find_winner(bidders_data)
    elif more_bidders=="yes":
        os.system('cls')
