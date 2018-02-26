class Clothing(object):

    def __init__(self, name, color, clean=True):
        self.name = name
        self.color = color
        self.clean = clean

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def isClean(self):
        return self.clean

    def setClean(self, state):
        self.clean = state

    def  __repr__(self):
        return "clothing[name=" + self.name + ", color=" + self.color + ", clean=" + str(self.clean)
