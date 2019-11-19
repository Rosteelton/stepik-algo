from pylab import *
from numpy import *
import matplotlib.pyplot as plt


if __name__ == '__main__':
    x = linspace(0.1, 2, 20)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(x, 4**x, label="y = 4^n")
    ax.plot(x, x*(log2(x))**3, label="y = n(log2n)^3")
    ax.legend(loc=2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('functions')
    show()