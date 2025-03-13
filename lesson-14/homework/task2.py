import numpy as np

def power(base, exponent):
    return base ** exponent

vectorized_power = np.vectorize(power)

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])

result = vectorized_power(bases, exponents)

print("Result:", result)