import matplotlib.pyplot as plt
import numpy as np

from .evalfis import evalfis

def gensurf(fis):

    plt.xlim(fis.Inputs[0].Range)
    plt.xlabel(fis.Inputs[0].Name)
    plt.ylabel(fis.Outputs[0].Name)

    x = np.linspace(fis.Inputs[0].Range[0], fis.Inputs[0].Range[1], 101)
    y = evalfis(fis, x)

    plt.plot(x, y)
    plt.show()
