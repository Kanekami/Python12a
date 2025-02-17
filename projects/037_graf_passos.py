import matplotlib.pyplot as plt
import numpy as np
list_steps=[]
list_steps.append([0,0,0,0.0])

while True:
    a=input("Add number of steps? (s/n)")
    if a == "s":
        steps=(int(input("Number of Steps: ")))
        hours=(int(input("Hours: ")))
        minutes=(int(input("Minutes: ")))
        t=hours+minutes/60
        list_steps.append([steps, hours, minutes, t])
    else:
        break

xpoints = [item[3] for item in list_steps]
ypoints = [item[0] for item in list_steps]

print("Lista de passos:")
for k in range(len(list_steps)):
    print(
        f"{list_steps[k][0]} passos às {list_steps[k][1]:02}:{list_steps[k][2]:02}"
    )

plt.xlabel("x")
plt.ylabel("y")
plt.title("Pontos (x,y)")
plt.xlim(0,24)
plt.scatter(xpoints, ypoints, color="blue", s=100)
plt.plot(xpoints, ypoints)
plt.show()