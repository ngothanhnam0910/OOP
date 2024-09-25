# Define a class Car with attributes
class Car:
    def __init__(self, make, model, year):
        self.make = make   # attribute: make
        self.model = model  # attribute: model
        self.year = year    # attribute: year
        self.odometer = 0  # attribute: odometer reading, initialized to 0 by default
        
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def drive(self, miles):
        self.odometer += miles

# Creating instances of the Car class
my_car = Car("Toyota", "Camry", 2022)
your_car = Car("Honda", "Accord", 2023)

# Accessing attributes using dot notation
print(my_car.make)    # Output: Toyota
print(your_car.model) # Output: Accord

# Calling methods on the instance
my_car.display_info()   # Output: 2022 Toyota Camry

my_car.drive(100)       # Drive 100 miles
print(my_car.odometer)  # Output: 100