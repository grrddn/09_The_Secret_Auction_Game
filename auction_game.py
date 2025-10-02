def auction_game():
    auction = {}
    bidders = True

    while bidders == True:
      name = input("Type in your name please: \n")
      bid = int(input("Type in your bid please: \n"))
      auction[name] = bid
      bidders = input("Are there anymore bidders? Type 'yes' or 'no': \n").lower()

      if bidders == "no":
        bidders = False
      else:
        bidders = True
        print("\n" * 10)

    highest_bid = 0
    for i in auction:
      if auction[i] > highest_bid:
        highest_bid = auction[i]
        winner = i

    print(f"The winner is {winner} with a bid of {highest_bid}")