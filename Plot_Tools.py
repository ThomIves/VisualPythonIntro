import matplotlib.pyplot as plt
import sys


def Basic_Plot(x=None, y=None,
               t='Title',
               x_t='X Points',
               y_t='Y Points',
               xp=None, yp=None):

    if x is not None and y is not None:
        plt.plot(x, y)
    plt.title(t)
    plt.xlabel(x_t)
    plt.ylabel(y_t)
    if xp is not None and yp is not None:
        plt.scatter(xp, yp)
    plt.show()
