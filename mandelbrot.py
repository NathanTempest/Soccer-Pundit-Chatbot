import numpy as np
import matplotlib.pyplot as plt

# Define the function to check if a point is in the Mandelbrot set
def in_mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter

# Generate x and y values
x = np.linspace(-2.5, 1.5, 1000)
y = np.linspace(-1.5, 1.5, 1000)

# Create a meshgrid of x and y values
X, Y = np.meshgrid(x, y)

# Create an empty array to store the Mandelbrot set
mandelbrot_set = np.zeros_like(X, dtype=int)

# Iterate over each point in the meshgrid
for i in range(len(x)):
    for j in range(len(y)):
        c = X[i, j] + 1j * Y[i, j]
        mandelbrot_set[i, j] = in_mandelbrot(c, 100)

# Plot the Mandelbrot set
plt.imshow(mandelbrot_set, extent=[-2.5, 1.5, -1.5, 1.5], cmap='viridis')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Mandelbrot Set')
plt.show()

x = np.linspace(-0.5, 0.5, 1000)
y = np.linspace(-0.5, 0.5, 1000)

