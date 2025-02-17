passos= []
total=0
while True:
    a=input("Deseja passos? (s/n)")
    if a=="s":
        passos.append([input("nº de passos: "), int(input("horas: "), int(input("minutos: ")))])
    else:
        break

for k in range(len(passos)):
    print(f"{passos[k][0]} passos as {passos[k][1]:02}:{passos[k][2]:02}")