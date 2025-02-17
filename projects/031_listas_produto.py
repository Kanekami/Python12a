produtos= [
    ["playstation 5", 500],
    ["Rato Razor Deathadderr", 500],
    ["X-Box", 50],
    ["Bicicleta", 800]
]
preço_total=0
for k in range(len(produtos)):
    print(f"{produtos[k][0]} --- {produtos[k][1]}")
    preço_total+=produtos[k][1]
print(f"Preço Total: {preço_total}")
s