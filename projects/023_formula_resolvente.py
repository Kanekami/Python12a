import math

print("introduza uma equação de segundo grau")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

delta = b ** 2 - 4 * a * c
if delta >= 0:
    x_1 = (-b + math.sqrt(delta)) / (2 * a)
    x_2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"x={x_1} ∨ x={x_2}")
else:
    print("A equação não tem soluções reais")
