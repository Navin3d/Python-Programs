num1 = int(input("Enter Smallest Number : "))
num2 = int(input("Enter Largest Number : "))
for i in range(1, num1+1):
    if num1%i==0 and num2%i==0:
        gcd = i
print(gcd)
