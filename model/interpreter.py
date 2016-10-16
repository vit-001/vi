# -*- coding: utf-8 -*-
__author__ = 'Nikitin'

from model.data import Data
from datetime import datetime

# Формат входного файла:
# #..... - комментарий

# AVP - добавить подэкран

# ACS(name)n - добавить свечки на подэкран n
# CS(name):date time;open;high;low;close

# AG(name)n - добавить график на подэкран n
# (name):date time;value - график

# AD(name)n:marker='o' markersize=10 - добавить массив точек на подэкран n
# (name):date time;value - точка


class Interpreter:
    def __init__(self, debug=False):
        self.data=Data()
        self.debug=debug

    def proceed(self,file):
        n=0
        print('Запускаем интерпретатор')
        for line in file:
            n+=1
            if self.debug: print('=====Строка',n,'=====')
            line=line.strip()

            if line.startswith('#'):
                print(line.lstrip("#"))
                continue

            (key,sp,data)=line.partition(":")
            if self.debug: print(key,data)

            if key=="AVP": # добавляем подэкран
                self.data.new_viewport()
                continue

            if key.startswith("ACS"): # добавляем график свечек
                name=self._get_name(key)
                vp=int(key.partition(')')[2])
                self.data.new_candle(vp,name)
                continue

            if key.startswith("CS"): # добавляем значения свечек
                name=self._get_name(key)
                split=data.split(';')
                time = datetime.strptime(split[0], "%Y.%m.%d %H:%M:%S")
                self.data.add_candle(name,time,float(split[1]),float(split[2]),float(split[3]),float(split[4]))
                continue

            if key.startswith("AG"): # добавляем график линию
                name=self._get_name(key)
                vp=int(key.partition(')')[2])
                self.data.new_graph(vp,name)
                continue

            if key.startswith("AD"): # добавляем график точки
                name=self._get_name(key)
                vp=int(key.partition(')')[2])
                options=self._get_options(data)

                self.data.new_dots(vp,name,options)
                continue

            if key.startswith("("): # добавляем значения точек или линии
                name=self._get_name(key)
                split=data.split(';')
                time = datetime.strptime(split[0], "%Y.%m.%d %H:%M:%S")
                self.data.add_value(name,time,float(split[1]))
                continue

            print("Ошибка в строке",n,":")
            print("  ",line)
            print('   Неизвестный ключ:',key)

        print('====================')
        print("Обработано",n,"строк")
        return self.data

    def _get_name(self,txt):
        return txt.partition("(")[2].partition(')')[0]

    def _get_options(self,txt):
        split=txt.split(' ')
        # print(split)
        options=dict()
        for item in split:
            (key,sp,data)=item.partition('=')
            options[key]=data.strip('"').strip("'")
        # print(options)
        return options

if __name__ == "__main__":
    pass