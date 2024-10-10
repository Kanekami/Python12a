import os

#os.system("cls")

print("Tabuada")
print("Escolha um numero inteiro")
a=input()
try:
    number=int(a)
except ValueError:
    number=float(a)

for x in range (1, 11):
    print(number * x)