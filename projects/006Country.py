print("Qual e o teu nome?")
name = input()
print("Qual 'e a tua nacionalidade? (Espanha, Alemanha, França...)")
country = input()
if country.lower()== "espanha":
    print(f"Hola, {name}!")
elif country.lower()== "alemanha":
    print(f"Guten Tag, {name}!")
elif country.lower()== "frança":
    print(f"Bonjour, {name}!")
else:
    print(f"Olá, {name}!")