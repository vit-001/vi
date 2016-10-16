# -*- coding: utf-8 -*-
__author__ = 'Nikitin'


class Data:
    def __init__(self, debug=False):
        self.debug=debug

        self.viewports = list()
        self.candles = dict()
        self.graphs = dict()
        self.dots=dict()

        self._names = list()

    def new_viewport(self):
        self.viewports.append(dict())  # добавляем пока пустой список меток графиков
        if self.debug: print("New viewport")

    def new_candle(self, vp, name):
        self._add_name(name)
        self._test_vp(vp)

        candle = dict()
        options = dict()
        options['data'] = candle
        self.candles[name] = candle
        self.viewports[vp][name] = options

        if self.debug: print("New candle", vp, name)

    def add_candle(self, graph_name, time, open, high, low, close):
        if self.debug:  print("CS:", time, open, high, low, close)
        if graph_name not in self.candles:
            raise RuntimeError("Ошибка данных: не определен график свечей " + graph_name)

        self.candles[graph_name][time] = (open, high, low, close)

    def new_graph(self, vp, name):
        self._add_name(name)
        self._test_vp(vp)

        data=dict()
        options=dict()

        self.graphs[name]=data
        self.viewports[vp][name]=options

        if self.debug: print("New graph", vp, name)

    def add_graph(self, name, time, value):
        if self.debug: print("Add graph", name, time, value)
        if name not in self.graphs:
            raise RuntimeError("Ошибка данных: не определен график " + name)
        self.graphs[name][time] = value

    def new_dots(self, vp, name,options):
        self._add_name(name)
        self._test_vp(vp)

        data=dict()

        self.dots[name]=data
        self.viewports[vp][name]=options

        if self.debug: print("New dots", vp, name)

    def add_dot(self, name, time, value):
        if self.debug: print("Add dot", name, time, value)
        if name not in self.dots:
            raise RuntimeError("Ошибка данных: не определен массив точек " + name)
        self.dots[name][time] = value

    def add_value(self,name,time,value):
        if name in self.graphs:
            if self.debug: print("Add graph", name, time, value)
            self.graphs[name][time] = value
            return
        if name in self.dots:
            if self.debug: print("Add dots", name, time, value)
            self.dots[name][time] = value
            return
        raise RuntimeError("Ошибка данных: не определен график " + name)

    def _add_name(self, name):
        if name in self._names:
            raise RuntimeError("Ошибка данных: повторное определение " + name)
        self._names.append(name)

    def _test_vp(self,vp):
        if vp >= len(self.viewports):
            raise RuntimeError("Ошибка данных: подэкран " + vp.__str__() + " не определен")

if __name__ == "__main__":
    pass