import unicodedata
print("Sim ou Não?")

options=("sim", "nao", "nim")
k=input().lower()

while k not in options: #k!=1 or k!=2 or k!=3
    k= (input("n.º invalido um nº de 1 a 3: ")).lower()

print("numero inserido com sucesso")
print(k)

