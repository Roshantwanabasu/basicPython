from __future__ import print_function
import math

class Shape(): #parents
    def __init__(self):
        self.color = "red"
        self.sides = 0
    def calArea(self):
        return 0
class Square(Shape): #child
    def __init__(self,w,c):  #method overriding function
        Shape.__init__(self)
        self.width = w
        self.color = c
    def calArea(self):
        return self.width **2
class Circle(Shape): #child
    def __init__(self,r,c):  #method overriding function
        Shape.__init__(self)
        self.radius = r
        self.color = c
    def calArea(self):
        return self.radius * 2 * math.pi

sq1 = Square(5, "Green")
sq2 = Square(9, "Black")
c1 = Circle(11,"Orange")

print(sq1.color,sq1.sides,sq1.width)
print(sq2.color,sq2.sides,sq2.width)
print(c1.color,c1.sides,c1.radius)
print(c1.calArea())
print(sq1.calArea())