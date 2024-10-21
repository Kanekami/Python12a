print("Sim ou Não?")

options=("sim", "não", "nim")
k=input().lower()

while k not in options: #k!=1 or k!=2 or k!=3
    k= (input("Resposta invalido, sim ou não?")).lower()

if k=="sim" or k=="não":
    print(f"Claramente {k}")
elif k=="nim":
    print("Engraçadinho.")
