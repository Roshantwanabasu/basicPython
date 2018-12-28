import math
def maxNum(x):
    c = 0
    for a in x:

        if c < a:
            c = a
    print("the greatest no is:", c)

x = [2,5,16,35,9,1]
maxNum(x)

def calCircum(r):
    res = 0
    res = 2*math.pi*r
    print("the circumference is",round(res,2))

r = int(input("enter value of r:"))
calCircum(r)