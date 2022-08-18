import matplotlib.pyplot as plt
import fuzzylab as fl

def gensurf(fis):

    plt.xlim(fis.Inputs[0].Range)
    plt.xlabel(fis.Inputs[0].Name)
    plt.ylabel(fis.Outputs[0].Name)

    start, stop = fis.Inputs[0].Range

    x = fl.arange(start, 0.01, stop)
    y = fl.evalfis(fis, x)

    plt.plot(x, y)
    plt.show()
