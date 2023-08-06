def select_size():
    print("What size would you like?")
    print("--> type R for regular (500ml) €4")
    print("--> type L for large (700ml) €5")

    while True:
        smth_size = input("Enter size: \n").upper()
   
        if smth_size == "R":
            print("You chose regular")
            break
            # apend to class
        elif smth_size == "L":
            print("You chose large")
            break
            # apend to class
        else:
            print("Please choose either 'R' or 'L'")


select_size()