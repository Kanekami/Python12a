produtos=["Playstation 5", "Rato Razor Deathadder", "X-Box", "Bicicleta"]
preço=[500, 50, 600, 800]
a=0
for k in range(len(preço)):
   a+=preço[k]
print(a)
for k in range(len(preço)):
    print(f"{produtos[k]} --- {preço[k]}")
