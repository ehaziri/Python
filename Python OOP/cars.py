class Cars(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if(self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print "Price:" , self.price , "\nSpeed:", self.speed , "\nFuel:" , self.fuel , "\nMileage:" , self.mileage , "\nTax:" , self.tax , "\n"

c1 = Cars(2000, "35mph", "Full", "15mpg")
c2 = Cars(2000, "5mph", "Not Full", "105mpg")
c3 = Cars(2000, "15mph", "Kind of Full", "95mpg")
c4 = Cars(2000, "25mph", "Full", "25mpg")
c5 = Cars(2000, "45mph", "Empty", "25mpg")
c6 = Cars(200000000, "35mph", "Empty", "15mpg")
