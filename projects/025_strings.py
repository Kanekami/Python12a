import time
from collections import defaultdict


def pause(pause_time):
    time.sleep(pause_time)

input_string=input("Input String:").upper()
x_length=len(input_string)
print(f"String length = {x_length}")

print("Sem espaços")
for car in input_string:
    print(f"{car}", end="", flush= True)
    pause(0.1)

print("\nCom espaços")
for car in input_string:
    print(f"{car}", end=" ", flush= True)
    pause(0.1)

n_spaces=input_string.count(" ")
print(f"Numero de espaços no input: {n_spaces}.")
n_s=input_string.count(" ")
print(f"Numero de espaços no input: {n_s}.")

vogais="AÁÀÃÂEÉÈÊIÍÌÎOÓÒÕÔUÚÙÛ"
chars = defaultdict(int)
number_vogais=0
for char in input_string:
    if (char in vogais):
        number_vogais+=1
print(f"Numero de vogais no input: {number_vogais}.")