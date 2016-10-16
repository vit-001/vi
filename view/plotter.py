# -*- coding: utf-8 -*-
__author__ = 'Nikitin'
from model.data import Data
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick2_ohlc,candlestick_ohlc
from matplotlib.dates import date2num

class Plotter:
    def __init__(self, data=Data()):
        self.data=data

        print('Запускаем плоттер')
        self._vp_config()
        self._plot()
        plt.show()

    def _vp_config(self):
        f = plt.figure()
        plt.subplots_adjust(hspace=0.001,left=0.05,right=0.99, top=0.96, bottom=0.05)
        num_subplot=len(self.data.viewports)
        self.axises=list()

        ax1 = plt.subplot(num_subplot*100+11)
        self.axises.append(ax1)

        for i in range(num_subplot-1):
            ax = plt.subplot(num_subplot*100+i+12, sharex=ax1)
            self.axises.append(ax)

    def _plot(self):

        self._plot_candles()
        self._plot_graphs()
        self._plot_dots()


        # for item in (self.data.viewports):
        #     print(item.keys())
        # print(self.data.candles)
        # print(self.data.graphs)
        # print(self.data.dots)

    def _plot_candles(self):
        for candle_name in self.data.candles:
            # print(candle_name)
            candles=self.data.candles[candle_name]
            tohlc_list=list()
            for time in sorted(candles):
                t=list()
                t.append(date2num(time))
                t.extend(candles[time])
                tohlc_list.append(t)
                # print(time,candles[time],t)

            vp=self._find_vp(candle_name)
            # print(vp)
            # print(tohlc_list)
            candlestick_ohlc(self.axises[vp],tohlc_list,width=60.0*10/(24.0*3600.0)*0.8)#,alpha=a,colorup=cu,colordown=cd)

    def _plot_graphs(self):
        for graph_name in self.data.graphs:
            # print(graph_name)
            graph=self.data.graphs[graph_name]
            times=list()
            dates=list()
            for time in sorted(graph):
                # print(time,graph[time])
                times.append(time)
                dates.append(graph[time])

            vp=self._find_vp(graph_name)
            self.axises[vp].plot_date(times,dates,ls="-",marker=None)

    def _plot_dots(self):
        for dots_name in self.data.dots:
            # print(dots_name)
            dots=self.data.dots[dots_name]
            times=list()
            dates=list()
            for time in sorted(dots):
                # print(time,dots[time])
                times.append(time)
                dates.append(dots[time])

            vp=self._find_vp(dots_name)
            options=self.data.viewports[vp][dots_name]
            # print(options)
            self.axises[vp].plot_date(times,dates,ls="None",marker=options.get('marker','o'),markersize=options.get('markersize',10))

    def _find_vp(self,name):
        for i in range(len(self.data.viewports)):
            if name in self.data.viewports[i]:
                return i

        raise RuntimeError("Что-то случилось в процедуре Plotter._find_vp")




if __name__ == "__main__":
    pass