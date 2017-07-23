class Bikes(object):
    def __init__(self, price, max_speed, miles=0):
        print 'New Bike!'
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "Bike's price =", self.price, ", maximum speed =", self.max_speed, ", total miles =", self.miles
        return self
    def ride(self):
        print "Riding."
        self.miles += 10
        return self
    def reverse(self):
        if(self.miles >= 5):
            self.miles -= 5
            print "Reversing."
        else:
            print "Negative miles."
        return self

bike1 = Bikes(200, "25mph")
bike1.ride().ride().ride().displayInfo()

bike2 = Bikes(200, "25mph")
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bikes(200, "25mph")
bike3.reverse().reverse().reverse().displayInfo()
