import numpy as np
import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']

data = np.array([[5, 7, 6, 8], [3, 5, 7, 6], [2, 3, 5, 4]])  # Sample data

plt.bar(time_periods, data[0], label="Category A", color='r')
plt.bar(time_periods, data[1], bottom=data[0], label="Category B", color='g')
plt.bar(time_periods, data[2], bottom=data[0] + data[1], label="Category C", color='b')

plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()
