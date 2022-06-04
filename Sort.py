def kishore(n):
    root = n/2
    for i in range(10):
        root=(root+n/root)/2
        print("root : ", root)
        print("n : ", n)
    print(root)
a = int(input("Enter a Num for Root : "))
kishore(a)