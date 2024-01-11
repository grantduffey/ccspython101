bill = float(input("Total bill amount? "))
service = input("Level of service? ")
split = int(input("Split how many ways? "))
total = 0.0
tip = 0.0

if service.upper() == "GOOD":
    tip = bill*.2
    total = bill + tip

elif service.upper() == "FAIR":
    tip = bill*.15
    total = bill + tip


elif service.upper() == "BAD":
    tip = bill*.1
    total = bill + tip

else:
    print("Please describe your service as Good, Fair, or Bad")
    exit(0)

print("Tip amount: $%.2f" % tip)
print("Total amount: $%.2f" % total)
print("Amount per person: $%.2f" % (total/split))

