while True:
    try:
        print("let us solve the equation (x/2)/(x-y)")
        x = float(input("please enter a value for x:"))
        y = float(input("please enter a value for y:"))
        if (x == 0 or y == 0):
            break
        z = (x / 2) / (x - y)
        print("solving (x/z)/(x-y) for value x =", x, "and y:", y, "we get the result:", z)
        break
    except Exception as e:
        print(e)
        break