import numpy as np
import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.bar(products, sales, color=['red', 'green', 'blue', 'purple', 'orange'])
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Data")
plt.show()