def select_yoghurt():
    print("Which yoghurt would you like?")
    print("--> type D for dairy")
    print("--> type S for soya")

    while True:
        select_yoghurt = input("Enter choice: \n").upper() # ensures input is in uppercase

        if select_yoghurt == "D":
            print("You chose dairy yoghurt")
            break
            # apend to class
        elif select_yoghurt == "S":
            print("You chose soya yoghurt")
            break
            # apend to class
        else:
            print("Please choose either 'D' or 'S'")


select_yoghurt()