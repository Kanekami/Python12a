list_variables=[
    "-Class Name: ", "-Complexity: ",
    "-Melee: ",
    "-Ranged: ", "-Mobility: ",
    "-Healing: ", "-Protection: ",
    "-Conditions: ",
    "-Elemental Affinities: "
]
baseline = 4
List_abilities=["class name", "complexity", "melee", "ranged", "mobile", "Invalid(HealBot)","Invalid(Tank)", "invalid Conditions"]
def create_list():
    temp_list = [
    input("Class Name: "), #0
    input("Complexity: "), #1
    input("Melee: "), #2
    input("Ranged: "), #3
    input("Mobility: "), #4
    input("Healing: "), #5
    input("Protection: "), #5
    input("Conditions: "), #6
    input("Elemental Affinities: "),
    ]
    return temp_list
input_cc = create_list()
print("\nDate Inserted: ")
for k in range(len(input_cc)):
    print(f"{list_variables[k]}{input_cc[k]}")
for i in range(2, 7):
    if int(input_cc[i]) > baseline:
        if i <= 3:
            print(f"You are a good {List_abilities[i]} fighter.")
        elif i == 4:
            print(f"You are a Rogue.")
        elif i == 5:
            print(f"You are a HealBot.")
        elif i == 6:
            print(f"You are a Tank.")
print(f"Your Elemental Affinities are : {input_cc[7]}")