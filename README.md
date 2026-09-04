# Homework__Llerena
Assignment #1

For this project two classes were created to simulate a car dealership.
The following information can be found at Car.py:

Attributes:  

    manufacturer(str): Basically it is mark of the car  
    model(str): Model of the car,  
    year(int): Car generation,
    mileage(int or float): Accumulative miles,
    engine(str): Type of engine,
    transmission(str): Type of transmission\n
    drivetrain(str): Type of drive train
    mpg(float): Mpg stands for Miles per galon
    exteriorColor(str): Exterior Color
    interiorColor(str): Interior Color
    accident(bool): Whether or not vehicle has been involved in an accident
    price(float): Price of the car
    
Functions:  

    Paint: Function that takes a str input eNewColor and modify the attribute exteriorColor. 
    Repair: Takes two parameters: 1)part will be the part replaced, also used as a "activator" for match-case. 2)replacement will be the new value of self.(part you selected)
    Reupholster: Function to change a interior color. New value cannot be same as current interior color.
    Drive: Function that should add input number to self.miles
    ModifyPrice: Function to change car's price or reduce current price.
