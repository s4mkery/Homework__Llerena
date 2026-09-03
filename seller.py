class Seller:

    name = str
    rating= int | float
    inventory = []

    def __init__(self,name,rating,inventory):
        self.name = name
        self.rating = rating   
        self.inventory = inventory

    def buy(self):
        pass

    def sell(self):
        pass
with open('archivo.csv', mode='r', newline='') as carsitos:
    for fila in carsitos:
        print(fila)