# -*- coding: utf-8 -*-
__author__ = 'Nikitin'

if __name__ == "__main__":
    import sys
    from model.interpreter import Interpreter
    from view.time_plotter import Plotter

    path = 'C:/Program Files/Alpari Limited MT5/Tester/Agent-127.0.0.1-3000/MQL5/Files/SA_log/'
    fname = 'grafx.dat'

    vi = Interpreter()

    for item in sys.argv[1:]:
        if item.startswith('-path='):
            path = item.partition('=')[2]
        if item.startswith('-file='):
            fname = item.partition('=')[2]

    print(path+fname)

    try:
        file = open(path+fname)
        data=vi.proceed(file)
        plotter=Plotter(data)

    except (OSError, RuntimeError) as err:
        print(err)
        # raise err