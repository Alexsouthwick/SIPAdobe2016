class Bird():
    def __init__(self, species, wingspan, color):
        self.species= species
        self.wingspan= wingspan
        self.color= color

    def fly(self, speed, height):
        print("fly")
    def sing(self,volume):
        print("The "+ self.species + " sings with " + volume + " volume")

eagle= Bird("eagle", 50, "white")
eagle.fly (30,50)
eagle.sing(30)

