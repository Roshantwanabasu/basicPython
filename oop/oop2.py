from __future__ import print_function
import math

def circumference(radius):
    return math.pi * 2 * radius

circles = [["first circle",4.4,0],["second circle",3.7,0],["third circle",8.4,0]]
circles[0][2] = circumference(circles[0][1])
print(circles[0][2])