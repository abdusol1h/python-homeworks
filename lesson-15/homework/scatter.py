import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.scatter(x, y, color='blue', marker='o', alpha=0.7)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot of Random Points")
plt.grid()
plt.show()
