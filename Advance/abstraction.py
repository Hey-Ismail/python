# -------------#
# //*Abstraction --> It is used to hide irrelevant details from the user and show the details that are relevant to the users.
# abstract method -->that has a declaration but dose not have a implementation .
# Abstract classes --> A class that content one or more abstract methods


from abc import ABC, abstractmethod


class Car(ABC):  # making it an abstract base class.

    @abstractmethod  # Its says that this method is abstracted
    def display(self):
        pass


class Porsche(Car):

    # overriding abstract method
    def display(self, name, engine):
        self.name = name
        self.engine = engine
        return f"Model :{self.name}\nEngine :{self.engine} (Its a wonderful sports car)"


class Mercedes(Car):

    def display(self, name, engine):
        self.name = name
        self.engine = engine
        return f"Model: {self.name}\nEngine: {engine}\n(known for luxury, comfort, and safety)"


class Lamborghini(Car):

    def display(self, name, engine):
        self.name = name
        self.engine = engine
        return f"Model: {self.name}\nEngine: {engine}\n(known for high performance and exotic design)"


class McLaren(Car):

    def display(self, name, engine):
        self.name = name
        self.engine = engine
        return f"Model: {self.name}\nEngine: {engine}\n(known for technology and lightweight construction)"


# Usage example
porsche = Porsche()
print(porsche.display("911 GT3", "Twin-Turbocharged Flat-Six"))

mercedes = Mercedes()
print(mercedes.display("S-Class", "V8 Biturbo"))

lamborghini = Lamborghini()
print(lamborghini.display("Aventador", "V12"))

mclaren = McLaren()
print(mclaren.display("720S", "Twin-Turbocharged V8"))
