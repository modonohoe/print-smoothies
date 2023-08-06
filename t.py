def select_smoothie():
    # Reminds user of numbers and prompts 
    # User enters number of chosen smoothie
    # Number will choose corresponding index from list

    print("MAKE YOUR CHOICE:\n")
    print("1 = Tropical Dreamwave")
    print("2 = Berry Bliss")
    print("3 = Peanut Butter Power")
    print("4 = Strawbalicious Banana Blast")
    print("5 = Protein-Packed Choco Cherry")
    print("6 = Green Energy Boost")
    print("7 = Mango Magic Mix")
    print("8 = Pomegranate Passion")
    print("9 = Peaches and Cream")
    print("10 = print(smoothies) Power Pop\n")

    smoothies = ["Tropical Dreamwave", "Berry Bliss", "Peanut Butter Power",
                 "Strawbalicious Banana Blast", "Protein-Packed Choco Cherry",
                 "Green Energy Boost", "Mango Magic Mix", "Pomegranate Passion",
                 "Peaches and Cream", "print(smoothies) Power Pop"]

    # parse user input to use as an index number
    smth_choice = int(input("Enter smoothie number: "))
    
    if 1 <= smth_choice <= len(smoothies):
        smth_choice = smoothies[smth_choice - 1]
        print(smth_choice + " added to order\n")
        return smth_choice
    else:
        print("Invalid smoothie number. Please try again.")


select_smoothie()

