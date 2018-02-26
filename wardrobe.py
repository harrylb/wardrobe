from clothing import *
from jacket import *
from socks import *
from shirt import *

class Wardrobe():
    def __init__(self, myClothes):
        self.clothes = myClothes

    def addClothing(self, article):
        self.clothes.append(article)

    def viewAllClothes(self):
        allClothes=[]
        for i in range(len(self.clothes)):
            allClothes.append(str(self.clothes[i]))
        return allClothes

    def viewAllJackets(self):
        allJackets=[]
        for i in range(len(self.clothes)):
            if isinstance(self.clothes[i], Jacket):
                allJackets.append(str(self.clothes[i]))
        return allJackets

    def viewAllShirts(self):
        allShirts=[]
        for i in range(len(self.clothes)):
            if isinstance(self.clothes[i], Shirt):
                allShirts.append(str(self.clothes[i]))
        return allShirts

    def viewAllSocks(self):
        allSocks=[]
        for i in range(len(self.clothes)):
            if isinstance(self.clothes[i], Socks):
                allSocks.append(str(self.clothes[i]))
        return allSocks

    def findCleanClothing(self):
        cleanClothes = []
        for i in range(len(self.clothes)):
            if self.clothes[i].isClean():
                cleanClothes.append(str(self.clothes[i]))
        return cleanClothes

    def showDirty(self):
        showDirty = []
        for i in range(len(self.clothes)):
            if not self.clothes[i].isClean():
                showDirty.append(str(self.clothes[i]))
        return showDirty

    def showColor(self, color):
        showColor = []
        for i in range(len(self.clothes)):
            if self.clothes[i].getColor() == color:
                showColor.append(str(self.clothes[i]))
        return showColor

    def findClothingBySleeveLength(self, sleeves):
        sleevedclothes = []
        for i in range(len(self.clothes)):
            if isinstance(self.clothes[i], Shirt):
                if self.clothes[i].getSleeves() == sleeves:
                    sleevedclothes.append(str(self.clothes[i]))
        return sleevedclothes

    def cleanClothes(self):
        cleanClothes = []
        for i in range(len(self.clothes)):
            self.clothes[i].setClean(True)
            cleanClothes.append(str(self.clothes[i]))
        return cleanClothes

if __name__ == "__main__":
    main()
