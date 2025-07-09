import numpy as np
import matplotlib.pyplot as plt

# Objective function: simple convex quadratic
def objective(x):
    return x ** 2

# 1. Define range
x_min, x_max = -5.0, 5.0

# 2. Generate x values
inputs = np.arange(x_min, x_max, 0.1)

# 3. Compute corresponding y = f(x)
results = [objective(x) for x in inputs]

# 4. Plot the function
plt.plot(inputs, results, label='f(x) = x²')
plt.axvline(x=0.0, linestyle='--', color='red', label='Optimum at x=0')
plt.title("Objective Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
