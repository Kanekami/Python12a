import math


question = "Na equação x^2=4, x é igual a que?"
options = "a) 1, b) 2, c) 3, d) -2, e) √4, g) -√4"
right = 'b', 'd', 'e', 'g'

solutions = 2, -2, math.sqrt(4) -math.sqrt(4)

print(question)
print(options)
k = input().lower()

while k not in options:
    print("Opção inválida. Tente novamente.")
    print(options)
    k = input().lower()

if k in right or k in solutions:
    print("Correto")
else:
    print("Resposta incorreta. Tente novamente.")
