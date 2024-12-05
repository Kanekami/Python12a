import os
import time

def apagaecra():
    os.system('cls')

def pausa(tempo):
    time.sleep(tempo)

apagaecra()
fruta=input("fruta para comprar: ")
quantidade=int(input("quantas frutas: "))
kg=float(input("peso do objeto(em kg): "))

preco=kg*1.99

compras=[fruta,quantidade,kg,preco]
compras_if=["Fruta", "Quantidade", "Peso", "Preço total"]

tam=len(compras)

print("informações da compra")

for k in range(tam):
    print(f"{compras_if[k]}: {compras[k]}")

print("")

if compras[3] >= 50.0:
    print("Vai sair caro!")
elif compras[3] >= 1.0:
    print("Venha sempre!")
else:
    print("Não quer mais nada?")