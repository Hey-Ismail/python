# ---------------------#
# *The word polymorphism means having many forms.
# * In programming, polymorphism means the same function name (but different signatures) being used for different types.
# *The key difference is the data types and number of arguments used in function.


# polymorphism with classes
class Porsche:
    def model(self):
        return f"Porsche 911-GT3"

    def owner(self):
        return f"Porsche-Piëch family"

    def engine(self):
        return f"4.0-liter flat-six engine"

    def wheels(self):
        return "four wheel"

    def color(self):
        return "White"

    def power(self):
        return "500 horse-power"

    def price(self):
        return "$291,650"


class Mercedes:

    def model(self):
        return f"Mercedes-Maybach S-Class"

    def owner(self):
        return f"Daimler AG"

    def engine(self):
        return f"6.0-liter Twin-turbocharged V12 engine"

    def wheels(self):
        return "four wheel"

    def color(self):
        return "Onyx Black"

    def power(self):
        return "621 horse-power"

    def price(self):
        return "$235,450"


porsche = Porsche()
mercedes = Mercedes()

for specification in (porsche, mercedes):
    print(specification.model())
    print(specification.owner())
    print(specification.engine())
    print(specification.wheels())
    print(specification.color())
    print(specification.power())
    print(specification.price())


# polymorphism with inheritance
class Car:
    def intro(self):
        return "There are two types of car, one is sports car and another one is luxury car"


# *This process of re-implementing a method in the child class is known as Method Overriding.
class Porsche(Car):
    def intro(self):
        return "porsche is a wonderful sports car!!!"


class Mercedes(Car):
    def intro(self):
        return "mercedes is a luxury car"


class Lamborghini(Car):
    def intro(self):
        return "lamborghini is a sports car"


class Rolls_Royce(Car):
    def intro(self):
        return "Rolls-Royce is a luxury car"


car = Car()
print(car.intro())
porsche = Porsche()
print(porsche.intro())
mercedes = Mercedes()
print(mercedes.intro())
lamborghini = Lamborghini()
print(lamborghini.intro())
rolls_royce = Rolls_Royce()
print(rolls_royce.intro())
