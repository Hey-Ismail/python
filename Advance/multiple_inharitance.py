# ----------------------#
# //* Multiple inheritance --> When a class is derived from more than one base class it is called multiple Inheritance.
# //* The derived class inherits all the features of the base case.


class Car:

    def __init__(self, brand, owner, model, color, engine, wheel, price):
        self.brand = brand
        self.owner = owner
        self.model = model
        self.color = color
        self.engine = engine
        self.wheel = wheel
        self.price = price

    def display(self):
        return f"Brand :{self.brand}\nOwner :{self.owner}\nModel:{self.model}\nColor :{self.color}\nEngine :{self.engine}\nWheel :{self.wheel}\nPrice :{self.price}"


class Porsche(Car):

    def __init__(self, brand, owner, model, color, engine, wheel, price):
        super().__init__(brand, owner, model, color, engine, wheel, price)

    def display(self):

        return super().display()


class Mercedes(Car):
    def __init__(self, brand, owner, model, color, engine, wheel, price):
        super().__init__(brand, owner, model, color, engine, wheel, price)

    def display(self):
        return super().display()


porsche = Car(
    "Porsche", "Porsche–Piëch family", "Black", "911 GT3", "V8", "Alloy", "$10000000"
)
print(porsche.display())
print("----------------------")
mercedes = Car("Mercedes", "Daimler AG", "Black", "AMG GT", "V8", "Alloy", "$140967409")
print(mercedes.display())
