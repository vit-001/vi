# -*- coding: utf-8 -*-
__author__ = 'Vit'

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from model.hist3ddata import Hist3dData

class Plotter:
    def __init__(self, data=Hist3dData(), nx=10, ny=10):
        self.data=data

        self.nx=nx
        self.ny=ny

        print('Запускаем плоттер')
        # self._config()
        self._plot()
        plt.show()

    def _config(self):
        pass

    def _plot(self):

        hist, xedges, yedges = np.histogram2d(self.data.x_array, self.data.y_array, bins=10)#, range=[[0, 4], [0, 4]])

        # print(hist)
        # print(xedges)
        # print(yedges)

        dx=xedges[1]-xedges[0]
        dy=yedges[1]-yedges[0]
        dz = hist.flatten()

        # print (dx,dy)

        xpos, ypos = np.meshgrid(xedges[:-1] + dx/2.0, yedges[:-1] + dy/2.0)
        # print(xpos)
        # print(ypos)

        xpos = xpos.flatten('F')
        ypos = ypos.flatten('F')
        zpos = np.zeros_like(xpos)

        # print(xpos)
        # print(ypos)
        # print(zpos)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.bar3d(xpos, ypos, zpos, dx/2.0, dy/2.0, dz, color='b')

if __name__ == "__main__":

    import random

    data=Hist3dData()
    for i in range(1000):
        data.add_point(random.random(),random.random())

    p=Plotter(data)
