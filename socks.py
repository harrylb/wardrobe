from clothing import *

class Socks(Clothing):
    def __init__(self, name, color, clean, number):
        super().__init__(name, color, clean)
        self.number = number

    def getNumber(self):
        return self.number()

    def __str__(self):
        return (super().__str__() + ", Number=" + (str(self.number)) + "]")
