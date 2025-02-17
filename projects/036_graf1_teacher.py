import matplotlib.pyplot as plt
import numpy as np
x=[0, 6]
y=[0, 250]

while True:
    a=input("Queres adicionar mais pontos? (s/n)")
    if a == "s":
        x.append(float(input("x: ")))
        y.append(float(input("y: ")))
    else:
        break
xpoints = np.array(x)
ypoints = np.array(y)

print("Lista de pontos:")
for k in range(len(xpoints)):
    print(f"({xpoints[k]};{ypoints[k]})")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Pontos (x,y)")
plt.grid
plt.scatter(xpoints, ypoints, color="blue", s=100)
plt.show()