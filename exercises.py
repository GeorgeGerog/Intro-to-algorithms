import matplotlib.pyplot as plt
import numpy as np

x = np.linespace(0,1000,1000)
plt.scatter(x,x**1.01)
plt.show()