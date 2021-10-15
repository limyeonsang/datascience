# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:14:22 2021

@author: 82109
"""
# %%
import numpy as np
import matplotlib.pyplot as plt
from random import randint

# %%
fig, ax = plt.subplots()
fig.set_size_inches(7,7)

x = np.array([range(1,13)]).reshape(-1,1)
y = np.zeros(12)

hp, = ax.plot(x,y)
ax.set_ybound(0, 600)
ax.set_xticks(range(1,13))

for _ in range(0, 5000):
    y[randint(1,6)+randint(1,6)-1] = y[randint(1,6)+randint(1,6)-1] + 1
    hp.set_ydata(y)
    plt.pause(0.00001)

