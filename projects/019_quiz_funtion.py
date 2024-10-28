import os
import time

def clean():
    os.system("cls")


def validar(uax, ox, qx):
    uax = uax.replace(") ", "").replace("; ", "")
    while uax not in ox:
        print("\n")
        print("Opção inválida. Tente novamente.")
        print(qx)
        uax = input().lower()
    return uax


def questionx(question, options, valid_x, x, answers):
    global points
    print(question)
    print(options)
    user_input = input().lower()
    user_input = validar(user_input, valid_x, question)
    if user_input in answers:
        points += x
        print("Acertaste!")
    else:
        print("Falhaste!")

print("Para cada pergunta, determine o valor de x.")

question_1 = "x + 1 = 2"
options_1 = "a) 1; b) 2; c) 3; d) 4; e) 5"
valid_1 = "abcde"
answer_1 = "a"
questionx(question_1, options_1, valid_1, 10, answer_1)

question_2 = "√x = 2"
options_2 = "a) 1; b) 4; c) 3; d) (-2)^2; e) 5"
valid_2 = "abcde"
answer_2 = ["b", "d"]

questionx(question_2, options_2, valid_2, 20, answer_2)

question_3 = "x^2 = 4"
options_3 = "a) 2; b) -2; c) √4; d) √-4; e) -√4; f) 1; g) 0"
valid_3 = "abcdefg"
answer_3 = ["a", "b", "c", "d", "e"]

questionx(question_3, options_3, valid_3, 30, answer_3)

print(f"Tiveste {points} pontos.")
print(f"O que corresponde a {points/60*100}%")
for k in range(30):
    time.sleep(0.1)
    print(".", end="", flush=True)

time.sleep(0.1)
print("!\n")