class Car():
    
    
    def __init__(self, make, model, year, horsepower):
        self.make = make
        self.model = model
        self.year = year
        self.horsepower = horsepower
        
    def showMake(self):
        print(f"The make of this car is {self.make}")
    
    def showHorsePower(self):
        print(f"The horsepower of this car is {self.horsepower}")
        

my_cars = []

for i in range(5):
    car = Car("Toyota", "Corolla", "2024", 700)
    my_cars.append(car)

for i in range(5):
    my_cars[i].showMake()

my_car = Car("Toyota", "Corolla", "2024", 700)
my_car.showMake()
my_car.showHorsePower()