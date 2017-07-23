class Animal(object):
    def __init__(self, name):
        print 'New Animal!'
        self.health = 100
        self.name = name
    def walk(self):
        print "Walk"
        self.health -= 1
        return self
    def run(self):
        print "Run"
        self.health -= 5
        return self
    def displayHealth(self):
        print self.name , "-->" , self.health
        return self

animal = Animal("animal")
# animal.fly()
# animal.pet()
