print("Validação de um imput de um nº de 1 a 3")


k = input("intruduza um nº de 1 a 3:")

options=("1", "2", "3")
while k not in options: #k!=1 or k!=2 or k!=3
    k = (input("n.º invalido um nº de 1 a 3: "))

print("numero inserido com sucesso")
print(k)