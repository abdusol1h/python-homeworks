import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

x = np.linspace(-2, 2, 400)

# Top-left: x^3
ax[0, 0].plot(x, x**3, color='r')
ax[0, 0].set_title("$f(x) = x^3$")
ax[0, 0].grid()

# Top-right: sin(x)
ax[0, 1].plot(x, np.sin(x), color='g')
ax[0, 1].set_title("$f(x) = \sin(x)$")
ax[0, 1].grid()

# Bottom-left: e^x
ax[1, 0].plot(x, np.exp(x), color='b')
ax[1, 0].set_title("$f(x) = e^x$")
ax[1, 0].grid()

# Bottom-right: log(x+1) for x >= 0
x_pos = np.linspace(0, 2, 400)
ax[1, 1].plot(x_pos, np.log(x_pos + 1), color='purple')
ax[1, 1].set_title("$f(x) = \log(x+1)$")
ax[1, 1].grid()

plt.tight_layout()
plt.show()