from animal import Animal
class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__("dragoi")
        self.health = 170
    def displayHealth(self):
        print "this is dragon!"
        super(Dragon, self).displayHealth()

    def fly(self):
        print "Fly"
        self.health -= 10
        return self

dragon = Dragon()
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
