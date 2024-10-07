import os

print("Escreve um nº entre 1 e 3, para o teu amigo adivinhar.")
number1 = input()

os.system("cls")

print("Qual foi o nº que o teu amigo escreveu?")
print("Dica: o nº esta entre 1 e 3.")
number2 = input()

if number1 == number2:
    print("Acertaste")
else:
    print("Falhaste")