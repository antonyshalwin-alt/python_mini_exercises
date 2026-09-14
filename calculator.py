def sum(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "ivalid"
    return a / b

num1 = float(input("enter the 1st number:"))
num2 = float(input("enter the 2nd number:"))

print(" SUM : ", sum(num1,num2))
print(" DIFFERENCE : ", substract(num1,num2))
print(" MULTIPLICATION : ", multiplication(num1,num2))
print(" DIVISION : ", division(num1,num2))

