# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 09:21:40 2021

@author: 82109
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 200)
y = np.linspace(0, 2*np.pi, 200)
grid_x, grid_y = np.meshgrid(x,y)
z = np.sin(grid_x)*np.sin(grid_y)

hfif = plt.figure()
hax = hfif.gca(projection='3d') # get current axis
hax.plot_surface(grid_x, grid_y, z, cmap='jet')
hax.set_xlabel('x')
hax.set_ylabel('y')
hax.set_zlabel('z')

# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 200)

sin = np.sin(x)

plt.plot(sin)
plt.show()
