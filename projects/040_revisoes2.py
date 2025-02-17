animais= [
]

while True:
    a=input("Queres adicionar mais animais? (s/n)")
    if a == "s":
        animais.append([input("Nome: "), int(input("Peso: ")), int(input("Longevidade:"))])
    else:
        break
for k in range(len(animais)):
    if 50 <= animais[k][2]:
        print(f"{animais[k][0]} Peso: {animais[k][1]}, Longevidade: {animais[1][2]}")
