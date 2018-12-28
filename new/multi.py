def tabMul(x,y):
    for a in range(1, x+1):
        for b in range(1, y+1):
            print (a * b, end="\t")
        print("\n")


x = int(input("enter x"))
y = int(input("enter y"))
tabMul(x,y)


