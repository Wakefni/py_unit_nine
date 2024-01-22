class Dog:
    def __init__(self, dogName):
        self.name = dogName
        self.trickList = []
    def getName(self):
        return self.name
    def sit(self):
        print(self.name, "sits")
        self.trickList.append("sit")
    def rollOver(self):
        print(self.name, "rolls over")
        self.trickList.append("roll over")
    def layDown(self):
        print(self.name, "lays down")
        self.trickList.append("lay down")

    def printTrickList(self):
        if not self.trickList:
            print(self.name, "has not performed any tricks yet.")
        else:
            print(self.name, "has performed the following tricks:")
            for trick in self.trickList:
                print(trick)


dog1 = Dog("Spot")
Dog


