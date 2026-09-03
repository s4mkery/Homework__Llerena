from car import Car
class Seller:

    name: str
    rating: int | float
    inventory = []

    def __init__(self,name,rating,inventory):
        self.name = name
        self.rating = rating   
        self.inventory = inventory

    def buy(self):


        newCar = Car(
            manufacturer=input("Manufacturer: "),
            model=input("Model: "),
            year=int(input("Year: ")),
            mileage=float(input("Mileage: ")),
            engine=input("Engine: "),
            transmission=input("Transmission: "),
            drivetrain=input("Drivetrain: "),
            mpg=float(input("MPG: ")),
            exteriorColor=input("Exterior Color: "),
            interiorColor=input("Interior Color: "),
            accident=input("Accident (yes/no): ").strip().lower() in ("yes"),
            price=float(input("Price: ")),
        )
        self.inventory.append(newCar)

        carDict = {
            "manufacturer": newCar.manufacturer,
            "model": newCar.model,
            "year": str(newCar.year),
            "mileage": str(newCar.mileage),
            "engine": newCar.engine,
            "transmission": newCar.transmission,
            "drivetrain": newCar.drivetrain,
            "mpg": str(newCar.mpg),
            "exteriorcolor": newCar.exteriorColor,
            "interiorcolor": newCar.interiorColor,
            "accident": str(newCar.accident),
            "price": str(newCar.price),
        }

        with open('Cars_Data.csv', mode='r', newline='') as cars:
            headers= [h.strip().lower() for h in cars]

        header = [carDict.get(col, "") for col in headers]
        boughtCar = ",".join(header) + "\n"

        with open("Cars_Data.csv", mode="a") as f:
            f.write(boughtCar)
            

            
    def sell(self, x):

        soldCar = self.inventory.pop(x)
        print("Sold car information: ")
        print(soldCar.manufacturer + " " + soldCar.model)
            
