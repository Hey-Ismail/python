# -------------------#
# //* Duck-type --> We do not need to check class at all. Instead, we check for the presence of a given method or attribute.
# The name Duck Typing comes from the phrase:
# //* “If it walk like a duck , and it quacks like a duck, then it must be a duck”


class Porsche:
    def model(self):
        print("Porsche 911-Gt3")

    def engine(self):
        print("4.0 litre six-cylinder engine ")


class Mercedes:
    def model(self):
        print("Mercedes-maybach s-class")

    def engine(self):
        print("6.0 liter twin Turbo Gas/Electric V-8")


class Tesla:
    def model(self):
        print("Tesla model-S")

    def is_electrical_engine(self):
        True


def display(anyobject):
    anyobject.model()
    anyobject.engine()


porsche = Porsche()
display(porsche)
mercedes = Mercedes()
display(mercedes)
# #! It will show error because tesla has a method that porsche and mercedes dont have
# tesla = Tesla()
# display(tesla)
