def kishore(n):
    root = n/2
    for i in range(10):
        root = (root+n/root)/2
    return root

num = int(input("Enter the number u wnat to find the root : "))
print(kishore(num))
