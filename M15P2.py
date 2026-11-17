# Kirill M15P2 11/16/2026

# Define class car
class Car():

# Define method for definding make, model, sticker price and discount price
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model 
        self.sticker_price = sticker_price
        self.discount_price = sticker_price * 0.90

# Define method for getting discount price
    def get_discount_price(self):
        return self.discount_price

# Define method for getting updated price
    def get_updated_price(self):
        return self.sticker_price

# Define method for displaying all methods 
    def display(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Sticker price:", self.sticker_price)
        print("Discount Price:", self.get_discount_price())
        print("Updated Price:", self.get_updated_price())

# Define a class SportCar as a inheritance for Car class
class SportCar(Car):

# Define method for definding make, model, sticker price, and sport options for SportCar
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = "Y"
        self.sport_engine = "Y"
        self.sport_interoir = "Y"

# Define specific value for each options for the sport car
    def get_updated_price(self):
        price = self.sticker_price
        if self.sport_wheels == "Y":
            price = price + 1000.00
        if self.sport_engine == "Y":
            price = price + 3000.00
        if self.sport_interoir == "Y":
            price = price + 2000.00
        return price 

# Define display method for showing each method of the sport car
    def display(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Sticker price:", self.sticker_price)
        print("Discount Price:", self.get_discount_price())
        print("Sport Wheels:", self.sport_wheels)
        print("Sport Engine:", self.sport_engine)
        print("Sport Interoir:", self.sport_interoir)
        print("Updated Price:", self.get_updated_price())

# Creating values for specific method
 
car1 = Car("Honda", "Civic Hatchback", 30000.00)
car2 = Car("Lada", "Sedan", 15000.00)

sc1 = SportCar("BMW", "M5", 150000.00)
sc2 = SportCar("Aston Martin", "DB12", 250000.00)

print()

# Display car1
car1.display()

print()

# Display car2
car2.display()


print()

# Display sc1
sc1.display()

print()

# Display sc2
sc2.display()

print()

# Displaying sc2 with additional value
sc2.sport_wheels
sc2.sport_engine
sc2.sport_interoir
sc2.display