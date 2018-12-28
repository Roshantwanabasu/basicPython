from __future__ import print_function

class Shape(): #parents
    def __init__(self):
        self.color = "red"
        self.sides = 0
class Square(Shape): #child
    def __init__(self,w):  #method overriding function
        Shape.__init__(self)
        self.width = w

sq1 = Square(5)
sq2 = Square(9)

print(sq1.color,sq1.sides,sq1.width)
print(sq2.color,sq2.sides,sq2.width)