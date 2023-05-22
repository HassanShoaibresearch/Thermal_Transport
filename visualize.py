import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits import mplot3d
import pdb


n_particles = 401 
n=np.arange(-(n_particles-1)/2, (n_particles-1)/2 + 1)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig=plt.figure()
ax=plt.axes(projection='3d')

directory='data'
test=os.listdir(directory)
u=np.zeros(n_particles)
#pdb.set_trace()
for item in test:
    if 'dump' in item:
        u=np.loadtxt(os.path.join(directory, item))
        t=np.ones(n_particles)*int(item.strip('.dump'))*2*np.pi*1e-2
        ax.plot(t, n, u[:,1], 'k')
        ax.set_ylabel(r'$n$')
        ax.set_xlabel(r'$t\omega_0$')
        ax.set_zlabel(r'$u$')

ax.azim = 50 
ax.elev = 30
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(False)
plt.show()
plt.savefig("displacement.pdf", format="pdf", bbox_inches="tight")
