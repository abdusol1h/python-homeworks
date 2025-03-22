import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 400)
sin_x = np.sin(x)
cos_x = np.cos(x)

plt.plot(x, sin_x, label="sin(x)", linestyle="--", color="r")
plt.plot(x, cos_x, label="cos(x)", linestyle="-.", color="b")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sine and Cosine Functions")
plt.legend()
plt.grid()
plt.show()