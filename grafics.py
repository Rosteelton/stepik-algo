from pylab import *
from numpy import *
import matplotlib.pyplot as plt


if __name__ == '__main__':
    x = linspace(0.1, 100000000000, 10000)
    fig, ax = plt.subplots(figsize=(5, 5))
    # ax.plot(x, log2(x), label="1")
    ax.plot(x, x ** 1.16094, label="2")
    # ax.plot(x, x ** 0.63, label="3")
    # ax.plot(x, x * x  * log2(x), label="4")
    ax.plot(x, x  * log2(x), label="5")
    # ax.plot(x, x ** 1.58, label="6")
    # ax.plot(x, x * x, label="7")
    # ax.plot(x, x ** 2.32, label="8")
    # ax.plot(x, x ** 3, label="9")
    ax.legend(loc=2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('functions')
    show()