prompt = ""
coins = 0

while prompt.upper() != "NO":
    print("You have %d coins." % coins)
    prompt = input("Do you want another? Type Yes or No ")
    if prompt.upper() == "YES":
        coins = coins + 1
    else:
        print("Please type Yes or No!")

print("Bye")