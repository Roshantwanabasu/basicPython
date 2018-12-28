def absoFun(val):
    if val < 0:
        val = val * -1
    return val






val = int(input("enter a value"))
x = absoFun(val)
print(x)