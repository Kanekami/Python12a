import time

points = 0

def validar(uax, ox, qx):
    uax = uax.replace(") ", "").replace("; ", "")
    while uax not in ox:
        print("\n")
        print("Opção inválida. Tente novamente.")
        print(qx)
        uax = input().lower()
    return uax

print("Para cada pergunta, determine o valor de x.")

q1 = "x + 1 = 2"
o1 = "a) 1; b) 2; c) 3; d) 4; e) 5"

print(q1)
print(o1)
ua1 = input().lower()
ua1 = validar(ua1, "abcde", q1)
if ua1 in ["a"]:
    points += 10

q2 = "√x = 2"
o2 = "a) 1; b) 4; c) 3; d) (-2)^2; e) 5"

print(q2)
print(o2)
ua2 = input().lower()
ua2 = validar(ua2, "abcde", q2)
if ua2 in ["b", "d"]:
    points += 20

q3 = "x^2 = 4"
o3 = "a) 2; b) -2; c) √4; d) √-4; e) -√4; f) 1; g) 0"

print(q3)
print(o3)
ua3 = input().lower()
ua3 = validar(ua3, "abcdefg", q3)
if ua3 in ["a", "b", "c", "d", "e"]:
    points += 30

print(f"Tiveste {points} pontos.")
print(f"O que corresponde a {points/60*100}%")
for k in range(30):
    time.sleep(0.1)
    print(".", end="", flush=True)

time.sleep(0.1)
print("!\n")