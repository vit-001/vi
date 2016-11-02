# -*- coding: utf-8 -*-
__author__ = 'Vit'


def _config_axis(min, max, n, opposite_n):
    for i in range(n):
        for j in range(opposite_n):
            print(i,j)


ax=_config_axis(0.,1.,3,5)

