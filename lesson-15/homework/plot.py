import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4  # Compute f(x)

# Plot the function
plt.plot(x, y, label=r"$f(x) = x^2 - 4x + 4$", color='b')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Plot of $f(x) = x^2 - 4x + 4$")
plt.legend()
plt.grid()
plt.show()