import functions

cc_variables=["-Nome do CC: ", "-Apelido do CC: ", "-Data de Nascimento do CC: ", "-Altura: "]
def create_cc():
    temp_list = [
    input("Nome do CC: "),
    input("Apelido do CC: "),
    input("Data de Nascimento do CC: "),
    float(input("Altura: "))
    ]
    return temp_list

input_cc = create_cc()
print("Dados Inseridos: ")
for k in range(len(input_cc)):
    print(f"{cc_variables[k]}{input_cc[k]}")

if input_cc[3] >= 1.80:
    print("És Alto.")
elif input_cc[3] >= 1.50:
    print("És Medio.")
else:
    print("Minorca.")