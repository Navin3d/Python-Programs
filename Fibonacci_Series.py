def fib(count):
    a = -1
    b = 1
    for i in range(count):
        c = a + b
        a = b
        b = c
        print(c)


n = int(input("Enter number of elements to be found : "))
fib(n)
