# -------------------#
# //* method overriding --> we can have multiple names
class Vehicle:
    def message(self):
        print("This message is from vehicle class")


class Car(Vehicle):

    def message(self):  # same name
        print("This message is from car class")


class Bike(Vehicle):

    def message(self):  # same name
        print("This message is from bike class")


# this is prioritize which one is closer from the object
vehicle = Vehicle()
vehicle.message()
car = Car()
car.message()
bike = Bike()
bike.message()
