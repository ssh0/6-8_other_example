#! /usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.
#
# 計算機実習
# 問題6.8 他の1次元写像その2
#

from math import *
import SetParameter  # 同じディレクトリ内にSetParameter.pyを置く必要がある
import myplot_6_8_iterate  # 同じディレクトリ内にmyplot_6_8_iterate.pyを置く必要がある


def func(x_i, r):
    return r * sin(pi * x_i)


def assignment():
    x0 = float(run.entry[0].get())
    r = float(run.entry[1].get())
    nmax = int(run.entry[2].get())
#    run.quit()
    myplot_6_8_iterate.plot(func, x0, r, nmax)

parameters = [{'x0': 0.4}, {'r': 0.8}, {'nmax': 50}]

if __name__ == '__main__':
    run = SetParameter.SetParameter()
    run.show_setting_window(parameters, {'OK': assignment})
