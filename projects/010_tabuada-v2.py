import os
#os.system("cls")
print("Tabuada")
while 1==1:
    print("Escolha um numero inteiro")
    a=input()
    try:
        a_int = int(a)
        #print(a_int)
    except ValueError:
        try:
            a_int = float(a)
            #print(a_int)
        except ValueError:
            print("Não existe tabuada de um numero.")
    os.system("cls")

    print("Qual deve ser o alcance da tabuada(numero inteiro).")
    b=input()
    try:
        b_int=int(b)
        #print(b_int)
        for x in range(1, b_int + 1):
            result = a_int * x
            print(f"{a_int}x{x}={result}")
        break
    except ValueError:
        print("O alcance não pode ser um numero decimal.")