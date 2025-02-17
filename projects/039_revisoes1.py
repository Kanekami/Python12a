# Nome do aluno: Vasco Lope
# Turma: 12ºA

name=input("What is your name?")
valido=["n", "m", "t"]
while 1==1:
    time=input("What time it is?(n/m/t)")
    if time in valido:
        break
if time == "n":
    print(f"Boa Noite, {name}!")
elif time == "m":
    print(f"Boa Manha, {name}!")
else:
    print(f"Boa targe, {name}!")