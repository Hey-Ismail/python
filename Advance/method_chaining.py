# -------------------#
# //* Method-chaining --> calling multiple method sequentially


class Human:

    def eat(self):
        print("Human is eating!")
        return self  # Returning the current instance

    def sleep(self):
        print("human is sleeping!")
        return self  # Returning the current instance

    def work(self):
        print("Human is working!")
        return self  # Returning the current instance

    def repeat(self):
        print("human is repeating!")
        return self  # Returning the current instance


human = Human()
human.eat().work().sleep().repeat()  # chining
