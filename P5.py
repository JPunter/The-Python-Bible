films = {
    "Finding Dory": [3,5],
    "Avengers":[12,5],
    "Momento":[18,5],
    "Rush":[15,5]
    }

while True:
    
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        #Check user age

        if age >= films[choice][0]:
            seats = int(input("How many seats would you like?: ").strip())

            #Check remaining seats
            
            if seats <= films[choice][1]:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - seats
            else:
                print("Sorry, we don't have any space left for this film")
        else:
            print("You are too young to see that film")
    else:
        print("We don't have that film")
