book = {}
choice = 0
name = ""
phone = ""

while choice != 5:
    print("Electronic Phone Book\n=====================")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit\n")
    
    choice = int(input("What do you want to do? (1-5) | "))
    
    if choice == 1:
        name = input("Name: ")
        if name in book:
            print("Found entry for %s: %s\n" % (name, book[name]))
        else:
            print("\nName not found.\n")
    
    if choice == 2:
        name = input("Name: ")
        if name in book:
            update = input("Name already exists. Do you want to update phone number? (y/n) | ")
            if update.upper() == "N":
                print("\n")
                continue
            if update.upper() != "N" and update.upper() != "Y":
                print("\nPlease input a valid response next time.\n")
                continue
        phone = input("Phone Number: ")
        book[name] = phone
        print("\nEntry stored for %s.\n" % name)
    
    if choice == 3:
        name = input("Name: ")
        if name not in book:
            print("\nName not found.\n")
            continue
        del book[name]
        print("\nDeleted entry for %s\n" % name)
    
    if choice == 4:
        for i in book:
            print("Found entry for %s: %s" % (i, book[i]))
        print("\n")
    
    if choice > 5 or choice < 1:
        print("\nPlease input a valid choice\n")
        choice = 1
        continue