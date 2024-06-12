# -----------------#
# //* Multilevel inheritance -->  It allows a class to inherit properties and methods from multiple parent classes,
# //* forming a hierarchy similar to a family tree.


# Multilevel inheritance
class Vehicle:  # Base class
    def __init__(self, brand):
        self.brand = brand

    def display(self):  # which refers to the instance of the class.
        return f"Brand: {self.brand}"


class Car(Vehicle):  # Derived class
    def __init__(self, brand, owner, color, model):
        super().__init__(brand)  # initializing the brand attribute (Vehicle class)
        self.owner = owner
        self.color = color
        self.model = model

    def display(self):
        return f"{super().display()}\nOwner: {self.owner}\nColor: {self.color}\nModel: {self.model}"


class Porsche(Car):  # Derived class
    def __init__(self, brand, owner, color, model, engine):
        super().__init__(brand, owner, color, model)
        self.engine = engine

    def display(self):
        return f"{super().display()}\nEngine Type: {self.engine}"


class Wheels(Porsche):  # Derived class
    def __init__(self, brand, owner, color, model, engine, wheel):
        super().__init__(brand, owner, color, model, engine)
        self.wheel = wheel

    def display(self):
        return f"{super().display()}\nWheel Type: {self.wheel}"


# Create instances and display their attributes

vehicle = Vehicle("Porsche")
print(vehicle.display())
print("---------------------")
car = Car("Porsche", "Porsche–Piëch family", "Black", "911 GT3")
print(car.display())
print("---------------------")
porsche = Porsche("Porsche", "Porsche–Piëch family", "Black", "911 GT3", "V8")
print(porsche.display())
print("---------------------")
wheels = Wheels("Porsche", "Porsche–Piëch family", "Black", "911 GT3", "V8", "Alloy")
print(wheels.display())
