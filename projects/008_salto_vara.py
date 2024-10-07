print("SALTO A VARA")

while 1 == 1:
    number = input("Que altura saltaste?")
    try:
        number = float(number)
        if number > 6.26:
            print("Superaste o Recorde Mundial")
        elif number == 6.17:
            print("Igual ao 10 recorde mundial")
        elif number > 5.06:
            print("Melhor que o recorde feminino")
        elif number >= 4:
            print("Bom resultado")
        elif number >= 3:
            print("OK")
        elif number >= 2:
            print("E melhor mudares de mudalidade")
        elif number >= 1:
            print("Foste a alguma competição? Foste humilhado?")
        elif number > 0:
            print("Conseguiste saltar!!!")
        elif number == 0:
            print("Sabias que e suposto saltares?")
        else:
            print("Invalido")
        break
    except ValueError:
        print("Escreve um numero!!!")