# A simple line plot using numpy arrays

import matplotlib.pyplot as plt
import numpy as np

# Create an array of numbers from 0 to 9 inclusive
x = np.arange(10)
# Create an array of squares of these numbers
y = x**2

# Now plot them
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('A nice plot')
plt.show()