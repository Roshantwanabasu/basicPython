while True:
    try:
        print("let us solve the equation (x/2)/(x-y)")
        x = float(input("please enter a value for x:"))
        y = float(input("please enter a value for y:"))
        if (x == 0 or y == 0):
            break

        z = (x / 2) / (x - y)


    except Exception as e:
        print("there was an error")

    except NameError as e:
        print("there was an error with the code")
        print("you keyed in a text value where a number was expected")

    except ZeroDivisionError as e:
        print("there was an error with the code")
        print("you keyed un a value that caused a division by zero")
    else:
        print("solving (x/z)/(x-y) for value x =", x, "and y:", y, "we get the result:", z)

    finally:
        print("clean up code goes here!!")
