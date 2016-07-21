class Dog():

    def __init__(self, furColor, weight, eyeColor,name):
        self.furColor = furColor
        self.weight = weight
        self.eyeColor = eyeColor
        self.name = name

    def bark(self):
        print("Woof")

    def wag(self):
        print("Wagging tail")

    def run(self):
        print("Dog is running")


Toto= Dog("Brown", 25, "Blue", "Toto")

Toto.bark()
Toto.wag()
Toto.run()
