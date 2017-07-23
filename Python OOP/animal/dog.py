from animal import Animal
class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("Qeni")
        self.health = 150
    def pet(self):
        print "Pet"
        self.health += 5
        return self

dog = Dog()
dog.walk().walk().walk().run().run().pet().displayHealth()
