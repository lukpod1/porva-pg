import matplotlib.pyplot as plt
import numpy as np 

figsize = [7,7]

fig, ax = plt.subplots()

b1, b2 = np.array([1, 0]), np.array([0, 1])
beta1, beta2 = np.array([2, 3]), np.array([-1, 1])

ax.arrow(0, 0, b1[0], b1[1] , fc='b', ec='b', head_width=0.3, head_length=3)
ax.arrow(0, 0, b2[0], b2[1] , fc='b', ec='b', head_width=0.3, head_length=3)
ax.arrow(0, 0, beta1[0], beta1[1] , fc='r', ec='c', head_width=0.3, head_length=3)
ax.arrow(0, 0, beta2[0], beta2[1] , fc='r', ec='c', head_width=0.3, head_length=3)
ax.axis([-3, 4, -5, 4])
ax.set_aspect('equal')
ax.axhline(color='k', alpha=.3)
ax.axvline(color='k', alpha=.3)
fig.set_size_inches(figsize)

plt.show()