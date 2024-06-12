# -------------------#
# //* Inheritance --> enables classes to share properties and methods by deriving from other classes.


# inheritance --> code reusability
class Car:  # Parent class

    def __init__(self, brand, owner, color, model):
        self.brand = brand
        self.owner = owner
        self.color = color
        self.model = model

    def display(self):
        return f"Brand: {self.brand}\nOwner: {self.owner}\nColor: {self.color}\nModel: {self.model}"


class ElectricCar(Car):  # Child class

    def __init__(self, brand, owner, color, model, battery_size):
        super().__init__(
            brand, owner, color, model
        )  # Call the constructor of the parent class
        self.battery_size = battery_size

    def display(self):
        parent_display = super().display()  # Get display method from the parent class
        return f"{parent_display}\nBattery Size: {self.battery_size} kWh"


# Creating an instance of Car
porsche = Car("Porsche", "Porsche–Piëch family", "Black", "911 GT3")
print(porsche.display())

print("\n---------------------\n")
# Creating an instance of ElectricCar
tesla = ElectricCar("Tesla", "Elon Musk", "White", "Model S", 100)
print(tesla.display())
