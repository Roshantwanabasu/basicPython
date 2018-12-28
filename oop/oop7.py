from __future__ import print_function
import math
import random
class Circle:
    def calCircumference(self):
        return math.pi * 2 * self.radius
    def calDiameter(self):
        return self.radius * 2
    def calArea(self):
        return math.pi * (self.radius **2)
    def __init__(self): #constructor function called
        self.radius = random.uniform(1.1,10.9)
circles= []
for i in range(0,10):
    c = Circle()
    #c.radius = random.uniform(1.1,10.5)
    #c.circumference = c.calCircumference()
    #obj cannot called in rhs of the operator
    circles.append(c)

for c in circles:
    print("Radius:",round(c.radius,2),"circumference:",round(c.calCircumference(),2),"Diameter:",round(c.calDiameter(),2),"area:",round(c.calArea(),2))