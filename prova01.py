import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as pactches

# x = [0,4.24,4.24,0,-4.24,-4.24,0]
# y = [6,4.24,-4.24,-6,-4.24,4.24,6]

# plt.plot( x, y, 'go') # green bolinha
# plt.plot( x, y, 'k:', color='orange') # linha pontilha orange

vertices = [
    (0,6),
    (6,3),
    (6,-3),
    (0,-6),
    (-6,-3),
    (-6,3),
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
patch = pactches.PathPatch(path, facecolor='white', lw=2)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.add_patch(patch)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
plt.grid(True)
plt.show()