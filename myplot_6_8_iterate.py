#! /usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.

import array as array
import matplotlib.pylab as plt


def plot(function, x0, r, nmax):
    x = array.array('d')
    x.append(x0)
    for i in range(nmax):
        x.append(function(x[i], r))
    n = range(nmax + 1)
    plt.plot(n, x, label=r'$x_{0}=$' + str(x0) + ' : '
             + '$r=$' + str(r) + ' : '
             + '$n_{\mathrm{max}}=$' + str(nmax)
             )
    plt.gca().set_xlim(0, nmax)
    plt.gca().set_ylim(min(x, 0.1) - 0.1, max(x) + 0.1)
    plt.xlabel(r'$n$', fontsize=16)
    plt.ylabel(r'$x$', fontsize=16)
    plt.title('map')
    plt.legend(loc="best")
    plt.show()
