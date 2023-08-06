from datetime import datetime, timedelta

smoothies = ["Tropical Dreamwave", "Berry Bliss", "Peanut Butter Power",
             "Strawbalicious Banana Blast", "Protein-Packed Choco Cherry",
             "Green Energy Boost", "Mango Magic Mix", "Pomegranate Passion",
             "python3 t.pyPeaches and Cream", "print(smoothies) Power Pop"]

# https://www.geeksforgeeks.org/python-datetime-timedelta-function/
# future feature could import timezone library

current_time = datetime.now()
collection_time = current_time + timedelta(hours=1.5) 

print("Your order will be available for collection TODAY from:\n")
print("            " + collection_time.strftime("%X") + "\n")