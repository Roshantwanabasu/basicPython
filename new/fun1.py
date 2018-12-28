



#defined function
def exp(x,y):
    z = x**y
    print(z)
def add(a,b):
    s = a+b
    print(s)

def fibo(strt,end,n):
    for x in range(0,n):
        print(strt)
        strt,end = end, strt+end
        #temp = strt
        #strt = end
        #end = temp + strt

def calfib(n):
    result = []
    a,b = 0,1
    while b<n:
        result.append(a)
        a,b = b,a+b
    return result

