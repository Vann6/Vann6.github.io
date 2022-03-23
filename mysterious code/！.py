import matplotlib.pyplot as plt

import numpy as np



init = np.arange(-np.pi, np.pi, 0.001)

y = np.subtract(np.multiply(2, np.cos(init)), np.cos(np.multiply(2, init)))

x = np.subtract(np.multiply(2, np.sin(init)), np.sin(np.multiply(2, init)))



plt.plot(x, y)

plt.fill_between(x, y, facecolor='red')

plt.show()
