#Travis the ridiculous security system

knownUsers = ["Alice", "Bob", "Charlie", "David", "Ed", "Frank", "Gary", "Henry"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    
    if name in knownUsers:
        print("Hello {}! Welcome!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()

        if remove == "y":
            knownUsers.remove(name)
            print("Thanks {}! You have been removed from the system".format(name))
        else:
            print("I hope you enjoy your continued membership!")
    else:
        print("I don't think we've met yet {}".format(name))
        add = input("Would you like to be added to the system (y/n)?: ").strip().lower()

        if add == "y":
            knownUsers.append(name)
            print("You have been added to our system!")
        else:
            print("OK")
        
    
