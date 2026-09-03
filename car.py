class Car:

    manufacturer: str
    model: str
    year: int
    mileage: int | float
    engine: str
    transmission: str
    drivetrain: str
    mpg: float
    exteriorColor: str
    interiorColor: str
    accident: bool
    price: float

    def __init__(self, manufacturer, model, year, mileage, engine, transmission, drivetrain, mpg, exteriorColor, interiorColor,
                 accident, price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine = engine
        self.transmission = transmission
        self.drivetrain = drivetrain
        self.mpg = mpg
        self.exteriorColor = exteriorColor
        self.interiorColor = interiorColor
        self.accident = accident
        self.price = price

    def Paint(self):
        while True:
                eNewColor = input("Introduce new car's exterior color: ")
        
                if self.exteriorColor != eNewColor:
                    self.exteriorColor = eNewColor
                    break
                else:
                    print("Invalid Input. Choose a diferent color")

    def Repair(self, part, replacement):  
        match part.strip().lower():
            case "engine":
                self.engine = replacement
            case "transmission":
                self.transmission = replacement
            case "drivetrain":
                self.drivetrain = replacement
            case _:
                print("Invalid part. Allowed parts for replacement: \nengine \ntransmission \ndrivetrain ")

    def Reupholster(self):  
        while True:
            iNewColor = input("Introduce new car's interior color: ")

            if self.interiorColor != iNewColor:
                self.interiorColor = iNewColor
                break
            else:
                print("Invalid Input. Choose a diferent color")
    
    def Drive(self):  
        while True:
                try:
                    miles = float(input("Introduce car's miles driven: "))
                    break
                except ValueError:
                    print("Input must be a valid number")

        self.mileage += miles
    
    def ModifyPrice(self): 
        while True:
            try:
                newPrice = float(input("Introduce car's new price: "))
                break
            except ValueError:
                print("Input must be a valid number")

        if newPrice >=1 :  
            self.price = newPrice
        else:
            self.price -= newPrice