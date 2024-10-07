import os

#os.system("cls")
a=float(input("Enter the first number: "))
equation=input("Enter the mathematical operation (+, -, *, /): ")
b=float(input("Enter the second number: "))

print("The result of", a, equation, b, "is", eval(str(a) + equation + str(b)))