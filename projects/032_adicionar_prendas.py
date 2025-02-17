produtos= [
    ["playstation 5", 500],
    ["Rato Razor Deathadderr", 500],
    ["X-Box", 50],
    ["Bicicleta", 800]
]
#preço_total=0
for k in range(len(produtos)):
    print(f"{produtos[k][0]} --- {produtos[k][1]}")
while True:
    a=input("Queres adicionar mais prendas? (s/n)")
    if a == "s":
        produtos.append([input("Prenda: "), int(input("Preço: "))])
    else:
        break
preco_total=0
for k in range(len(produtos)):
    print(f"{produtos[k][0]} --- {produtos[k][1]}")
    preco_total+=produtos[k][1]
print(f"Preço Total: {preco_total}")