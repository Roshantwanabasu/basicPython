from __future__ import print_function
import math
import random
class circle:
    def calCircumference(radius):
        return math.pi * 2 * radius
circles= []
for i in range(0,10):
    c = circle()
    c.radius = random.uniform(1.1,10.5)
    #c.circumference = c.calCircumference(c.radius)
    #obj cannot called in rhs of the operator
    circles.append(c)

for c in circles:
    print("Radius:",c.radius,"circumference:",c.circumference)