import matplotlib.pyplot as plt
import numpy as np
x=[0, 6]
y=[0, 250]

while True:
    a=input("Queres adicionar mais pontos? (s/n)")
    if a == "s":
        x.append(int(input("x: ")))
        y.append(int(input("y: ")))
    else:
        break
xpoints = np.array(x)
ypoints = np.array(y)

print("Lista de pontos:")
for k in range(len(xpoints)):
    print(f"({xpoints[k]};{ypoints[k]})")
plt.plot(xpoints, ypoints)
plt.show()