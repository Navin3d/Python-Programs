def factorial(n):
    fact = 1
    for i in range(n):
        fact *= n-i

    return fact

num = int(input("Enter a number: "))
print("The Factorial of the number is: ", factorial(num))
