paises= []
total=0
while True:
    a=input("Deseja adicionar algum pais? (s/n)")
    if a=="s":
        paises.append([input("Nome do pais: "), input("Capital do pais: "), int(input("População do pais: "))])
    else:
        break
for k in range(len(paises)):
    print(f"{paises[k][0]}")
    print(f"    Capital: {paises[k][1]}")
    print(f"    População {paises[k][2]}")
for k in range(len(paises)):
    total+=paises[k][2]
print(f"População Total: {total}")