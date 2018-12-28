import fun1

base = int(input("please enter a base value"))
expon = int(input("please enter a expon value"))
fun1.exp(base,expon)
aa = int(input("please a value"))
bb = int(input("please b value"))
fun1.add(aa,bb)


strt = int(input("please enter a base value"))
end = int(input("please enter a expon value"))
n = int(input("how many fibo series you want:"))
fun1.fibo(strt,end,n)


fibseries = fun1.calfib(23)
print(fibseries)