def valx(y,x,c):
    try:
        m = (y-c)/x
        print("the slope of straight line is:",m)
    except exception as e:
        print(e)
def aPlusaSq(a,b):
    print("the square of sum of a and b:",(a+b)**2)


y = int(input("give the y coord of the stline"))
x = int(input("give the x coord of the stline"))
c = int(input("give the constant value of the stline"))
valx(y,x,c)
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
aPlusaSq(a,b)
