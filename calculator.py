def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def modulus(x, y):
    return x % y

num1 = int(input("Enter the Number 1: "))
num2 = int(input("Enter the Number 2: "))
print("Addition : ", add(num1, num2))
print("Subtract : ", subtract(num1, num2))
print("Multiplication ", multiply(num1, num2))
print("Division : ", divide(num1, num2))
print("modules : ", modulus(num1, num2))
