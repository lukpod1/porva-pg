import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as pactches
x = [-3,3,6,3,-3,-6,-3]
y = [6,6,0,-6,-6,0,6]
plt.plot( x, y, 'go') # green bolinha
plt.plot( x, y, 'k:', color='orange') # linha pontilha orange
plt.grid(True)
plt.show()