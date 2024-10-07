print("Benfica")
number=input("Indique o numero da camisola do jogador: ")
try:
    number=int(number)
    if number == 1:
        print("Trubin")
    elif number == 24:
        print("Samuel S.")
    elif number == 75:
        print("A. Gomes")
    elif number == 3:
        print("A. Carreras")
    elif number == 4:
        print("António S.")
    elif number == 6:
        print("Bah")
    elif number == 28:
        print("Kaboré")
    elif number == 30:
        print("Otamendi")
    elif number == 37:
        print("Beste")
    elif number == 44:
        print("Tomás A.")
    elif number == 81:
        print("Bajrami")
    elif number == 8:
        print("Aursnes")
    elif number == 10:
        print("Kokcu")
    elif number == 18:
        print("Barreiro")
    elif number == 61:
        print("Florentino")
    elif number == 84:
        print("João Rego")
    elif number == 85:
        print("R. Sanches")
    elif number == 7:
        print("Amdouni")
    elif number == 9:
        print("A. Cabral")
    elif number == 11:
        print("Di María")
    elif number == 14:
        print("Pavlidis")
    elif number == 17:
        print("Akturkoglu")
    elif number == 21:
        print("Schjelderup")
    elif number == 25:
        print("Prestianni")
    elif number == 32:
        print("Rollheiser")
    elif number == 47:
        print("T. Gouveia")
    else:
        print("Não a jogadores no benfica com esse numero.")
        print("Fonte: https://www.slbenfica.pt/pt-pt/futebol/plantel-principal")
except ValueError:
    print("Escreve um numero!!!")