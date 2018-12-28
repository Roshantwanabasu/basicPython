#inheritance 6,7 & 8

from __future__ import print_function
import math

class Shape(): #parents
    def __init__(self):
        self.color = "red"
        self.sides = 0

    def calArea(self):
        return 0


class Quadrilateral(Shape):
    def __init__(self,w,l,c):
        self.sides = 4
        self.width = w
        self.length = l
        self.color = c

        def calArea(self):
            return self.width*self.length

class Square(Quadrilateral): #child

    def __init__(self,w,c):  #method overriding function
        Quadrilateral.__init__(self,w,w,c)

    def calArea(self):
        return self.width **2

class Circle(Shape): #child

    def __init__(self,r,c):  #method overriding function
        Shape.__init__(self)
        self.radius = r
        self.color = c

    def calArea(self):
        return self.radius * 2 * math.pi

class Triangle(Shape):

    def __init__(self,s1,s2,s3,c):
        Shape.__init__(self)
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.color = c

def printArea(s):
    print(s.calArea())

sq1 = Square(5, "Green")
sq2 = Square(9, "Black")
c1 = Circle(11,"Orange")
t1 = Triangle(3,4,5,"Purple")
print(sq1.color,sq1.sides,sq1.width)
print(sq2.color,sq2.sides,sq2.width)
print(c1.color,c1.sides,c1.radius)
print(c1.calArea())
print(sq1.calArea())
print(printArea(t1))