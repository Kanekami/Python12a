import math

n=int(input("Introduza um numero inteiro."))

n_fabs = int(math.fabs(n))
print(f"O valor absoluto do valor intruduzido e {n_fabs}.")
if n >= 0:
    n_fact = math.factorial(n)
    print(f"O fatorial do valor introduzido e {n_fact}.")