print("Escreve um numero entre 1 e 3, para o teu amigo adivinhar.")

#while 1 == 1:
number = input()
try:
    number1_int = int(number)
    if 1 <= number1_int <= 3:
        print("Qual foi o numero escrito?")
        number2 = input()
        try:
            number2_int = int(number2)
            if number1_int == number2_int:
                print("Acertou!")
            else:
                print("Errou!")
        except ValueError:
            print("Escreve um numero!!!")
           #break
    else:
        print("Escreve um numero entre 1 e 3")
except ValueError:
    print("Escreve um numero entre 1 e 3!!!")