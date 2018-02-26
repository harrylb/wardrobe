from clothing import *

class Jacket(Clothing):
    def __init__(self, name, color, clean, size, brand):
        super().__init__(name, color, clean)
        self.size = size
        self.brand = brand

    def getSize(self):
        return self.size()

    def getBrand(self):
        return self.brand()

    def __str__(self):
        return (super().__str__() + ", size=" + str(self.clean) + ", brand=" + self.brand + "]")
