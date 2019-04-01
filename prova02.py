import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as pactches

vertices = [
    (-3,6),
    (3,6),
    (6,0),
    (3,-6),
    (-3,-6),
    (-6,0),
    (0.,0.)
    
]
comandos = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY
]

path = Path(vertices, comandos)
patch = pactches.PathPatch(path, facecolor='blue', lw=2)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.add_patch(patch)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
plt.grid(True)
plt.show()