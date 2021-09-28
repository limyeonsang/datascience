# -*- coding: utf-8 -*-

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
fig, ax = plt.subplots()

x = np.array([1,2,3,4,5])
y = np.array([1,1,1,1,1])

hp, = ax.plot(x,y)
ax.set_ybound(0, 11)

for i in range(0, 11):
    hp.set_ydata(i*y)
    plt.pause(0.5)

# %%

