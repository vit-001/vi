# -*- coding: utf-8 -*-
__author__ = 'Vit'

import math

class DataIterator:
    def __init__(self,data):
        self._x_iter=data.x_array.__iter__()
        self._y_iter=data.y_array.__iter__()

    def __next__(self):
        return (self._x_iter.__next__(),self._y_iter.__next__())

class Hist3dData:
    def __init__(self):
        self.x_array=list()
        self.y_array = list()

    def add_point(self,x,y):
        self.x_array.append(x)
        self.y_array.append(y)

    @property
    def xmax(self):
        return max(self.x_array)

    @property
    def ymax(self):
        return max(self.y_array)

    @property
    def xmin(self):
        return min(self.x_array)

    @property
    def ymin(self):
        return min(self.y_array)

    def __iter__(self):
        return DataIterator(self)




if __name__ == "__main__":
    data=Hist3dData()

    data.add_point(1.,1.)
    data.add_point(2., 2.)

    for item in data:
        for jtem in data:
            print(item,jtem)