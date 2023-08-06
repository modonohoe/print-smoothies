smoothies = ["Tropical Dreamwave", "Berry Bliss", "Peanut Butter Power",
             "Strawbalicious Banana Blast", "Protein-Packed Choco Cherry",
             "Green Energy Boost", "Mango Magic Mix", "Pomegranate Passion",
             "Peaches and Cream", "print(smoothies) Power Pop"]

class Order:
    def __init__(self, customer, smoothie, _size, yoghurt, price):
        self.customer = customer
        self.smoothie = smoothie
        self._size = _size
        self.yoghurt = yoghurt
        self.price = price
    
    def ticket(self):
        print(f"{self.customer}'s order:")
        print(f"Smoothie(s): {self.smoothie}")
        print(f"Size(s): {self._size}")
        print(f"Yoghurt(s): {self.yoghurt}")
        print(f"Total: €{self.price}")


damo = Order("Damien", "Berry Blast", "reg", "soya", 5)
damo.ticket()