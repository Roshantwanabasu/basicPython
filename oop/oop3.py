from __future__ import print_function
import math

def circumference(radius):
    return math.pi * 2 * radius

class circle:
    pass

circle1 = circle()
circle1.radius = 4.4
print(circle1.radius)
print(circumference(circle1.radius))

circle2 = circle()
circle2.radius = 4
print(circle2.radius)
print(circumference(circle2.radius))

circle3 = circle()
circle3.radius = 8.4
print(circle3.radius)
print(circumference(circle3.radius))