class Seller:
from car import Car
class Seller:

    name: str
    rating: int | float
    inventory = []

    def _init_(self,name,rating,inventory):
        self.name = name
        self.rating = rating   
        self.inventory = inventory

    def buy(self):
        
        with open('Cars_Data.csv', mode='r', newline='') as cars:
            next(carsitos)

            for row in cars:

                atributes = row.strip().split(",")

                newCar = Car(
                    manufacturer=atributes[0],
                    model=atributes[1],
                    year=int(atributes[2]),
                    mileage=float(atributes[3]),
                    engine=atributes[4],
                    transmission=atributes[5],
                    drivetrain=atributes[6],
                    mpg=float(atributes[7]),
                    exteriorColor=atributes[8],
                    interiorColor=atributes[9],
                    accident=atributes[10].strip().lower() in ("yes", "1"),
                    price=float(atributes[11]),
                )
                self.inventory.append(newCar)

    def sell(self, x):

        soldCar = self.inventory.pop(x)
        print("Sold car information: ")
        print(soldCar.manufacturer + " " + soldCar.model)
