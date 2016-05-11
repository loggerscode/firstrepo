def fib(n):

    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def fib1(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

n = int(input("Gib ne Zahl ein.."))
for i in range(n):
    fib1(i)

print ("Ende")
