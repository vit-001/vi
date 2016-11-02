# -*- coding: utf-8 -*-
__author__ = 'Vit'


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xpos=(0.25,  0.25,  0.25,  0.25,  1.25,  1.25,  1.25,  1.25,  2.25,  2.25,  2.25,  2.25, 3.25,  3.25,  3.25,  3.25)
ypos=(0.25,  1.25,  2.25,  3.25,  0.25,  1.25,  2.25,  3.25,  0.25,  1.25,  2.25,  3.25, 0.25,  1.25,  2.25,  3.25)
zpos=( 10.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.)
dz=( 26.,  27.,  29.,  26.,  41.,  23.,  25.,  26.,  21.,  25.,  21.,  19.,  22.,  28.,  22.,  19.)

# dz = hist.flatten()

dx=0.5
dy=0.5

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b')#, zsort='average')

plt.show()