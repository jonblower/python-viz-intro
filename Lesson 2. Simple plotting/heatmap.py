# Script to plot a 2D array of data

import matplotlib.pyplot as plt
import numpy as np

# Create an array of x and y values
x = np.linspace(-1,1,11)
y = np.linspace(-1,1,11)
X, Y = np.meshgrid(x,y)

# Calculate values for each point
Z = np.cos(X) * np.cos(Y)

# Create and show filled contour plot
plt.contourf(x,y,Z,20)
plt.xlabel('x')
plt.ylabel('y')
plt.title('cos(x) * cos(y)')
plt.colorbar()
plt.show()