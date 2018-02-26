from clothing import *

class Shirt(Clothing):
    def __init__(self, name, color, clean, sleeves):
        super().__init__(name, color, clean)
        self.sleeves = sleeves

    def getSleeves(self):
        return self.sleeves

    def __str__(self):
        return (super().__str__() + ", sleeves=" + self.sleeves + "]")
