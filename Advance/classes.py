# ---------------#
# //* Classes --> A class is a user-defined blueprint or prototype from which objects are created.
class Car:

    wheel = 4  # class variable - outside declared

    def __init__(self, brand, owner, color, model):
        self.brand = brand  # instance variable - declared inside a constructor
        self.owner = owner  # instance variable
        self.color = color  # instance variable
        self.model = model  # instance variable


porsche = Car("Porsche", "Porsche–Piëch family", "Black", "911 GT3")  # object created
print(f"Brand: {porsche.brand}")
print(f"Owner: {porsche.owner}")
print(f"Color: {porsche.color}")
print(f"Model: {porsche.model}")
print(f"Wheel: {porsche.wheel}")
