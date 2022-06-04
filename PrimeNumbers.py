nterms = int(input("Enter the nth term : "))
count = 1
num = 1
while count <= nterms:
    for i in range(2, num):
        if num%i==0:
            break
    else:
        print(num)
        count += 1
    num = num+1
