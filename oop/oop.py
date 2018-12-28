from __future__ import print_function
import math

def circumference(radius):
    return math.pi * 2 * radius

circle1Name = "first circle"
circle1Radius = 4.4

circle2Name = "2nd circle"
circle2Radius = 3.0

circle3Name = "3rd circle"
circle3Radius = 4.4

circumference1 = circumference(circle1Radius)
print(circumference1, circle1Name)
circumference2 = circumference(circle2Radius)
print(circumference2, circle2Name)
circumference3 = circumference(circle3Radius)
print(circumference3, circle3Name)
