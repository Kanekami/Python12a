print("Bom dia, qual é o teu nome?")
nome = input()
print(f"Olá {nome}!")
print("Quantos anos tens?")
idade = input()
if idade.isnumeric():
    print(f"Olá {nome}. Tens {idade} anos de idade!")