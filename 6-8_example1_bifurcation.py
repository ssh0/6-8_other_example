#! /usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.
#
# 計算機実習
# 問題6.8その1

from math import *
import SetParameter  # 同じディレクトリ内にSetParameter.pyを置く必要がある
import myplot_6_8_bifurcation  # 同じディレクトリ内にmyplot_6_8_bifurcation.pyを置く必要がある


def assignment():
    def func(x_i, r):
        return x_i * exp(r * (1 - x_i))
    x0 = float(run.entry[0].get())
    ntransient = int(run.entry[1].get())
    nplot = int(run.entry[2].get())
    r0 = float(run.entry[3].get())
    rmax = float(run.entry[4].get())
    dr = float(run.entry[5].get())
    run.quit()
    myplot_6_8_bifurcation.Plot(func, x0, ntransient, nplot, r0, rmax, dr)

if __name__ == '__main__':
    run = SetParameter.SetParameter()
    parameters = [
        {'x0': 0.5}, {'ntransient': 1000}, {'nplot': 50}, {'r0': 1.5},
        {'rmax': 4.0}, {'dr': 0.001}]
    run.show_setting_window(parameters, {'OK': assignment})
