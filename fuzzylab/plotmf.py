import matplotlib.pyplot as plt
import numpy as np

from .evalmf import evalmf

def plotmf(fis, varType, varIndex, numPts=181):
    varType = varType[0].upper() + varType[1:] + 's'
    var = vars(fis)[varType][varIndex]
    numMFs = len(var.MembershipFunctions)

    x = np.linspace(var.Range[0], var.Range[1], numPts)
    y = np.zeros((numPts,numMFs))
 
    for mfIndex in range(numMFs):
        y[:, mfIndex] = evalmf(var.MembershipFunctions[mfIndex], x)

    plt.xlim(var.Range)
    plt.ylim([-0.1, 1.1])
    plt.xlabel(var.Name)
    plt.ylabel('Degree of membership')

    for mfIndex in range(numMFs):
        centerIndex = abs(y[:,mfIndex] - max(y[:,mfIndex])) < 1e-3
        xpos = np.mean(x[centerIndex])

        ax = plt.gca()
        canvas = ax.figure.canvas

        hText = ax.text(xpos, 1.03, var.MembershipFunctions[mfIndex].Name,
            horizontalalignment='center')
        hText.draw(canvas.get_renderer())

        ext = hText.get_window_extent()
        w_ext = ax.get_window_extent()

        if ext.x0 < w_ext.x0:
            hText.set_horizontalalignment('left')
            hText.set_position([var.Range[0] + 0.01 * np.diff(var.Range), 1.03])
        elif ext.x0 + np.diff([ext.x0, ext.x1]) > w_ext.x1:
            hText.set_horizontalalignment('right')
            hText.set_position([var.Range[1] - 0.01 * np.diff(var.Range), 1.03])
        
    plt.plot(x, y)
    plt.show()
