import matplotlib.pyplot as plt
import numpy as np

from .evalmf import evalmf

def plotmf(fis, variableType, variableIndex, numPoints=181, 
            fontSize=11.5, ylabel='Degree of membership', tex_out='', show=True,
            ggplot=False):

    assert variableIndex > 0, 'Expected input index to be positive.'
    
    if variableType.lower() == 'input':
        var = fis.Inputs[variableIndex - 1]
    else:
        var = fis.Outputs[variableIndex - 1]
    
    num_mfs = len(var.MembershipFunctions)

    x = np.linspace(var.Range[0], var.Range[1], numPoints)
    y = np.zeros((numPoints, num_mfs))
 
    for i in range(num_mfs):
        y[:, i] = evalmf(var.MembershipFunctions[i], x)

    if show and tex_out == '':
        plt.rcParams.update({'font.size': fontSize})
    if ggplot:
        plt.style.use("ggplot")

    plt.xlim(var.Range)
    plt.ylim([-0.1, 1.1])
    plt.xlabel(var.Name)
    plt.ylabel(ylabel)

    for i in range(num_mfs):
        center_index = abs(y[:,i] - max(y[:,i])) < 0.001
        x_pos = np.mean(x[center_index])

        ax = plt.gca()
        canvas = ax.figure.canvas

        h_text = ax.text(x_pos, 1.03, var.MembershipFunctions[i].Name,
            horizontalalignment='center', fontsize='small')
        h_text.draw(canvas.get_renderer())

        ext = h_text.get_window_extent()
        w_ext = ax.get_window_extent()

        if ext.x0 < w_ext.x0:
            h_text.set_horizontalalignment('left')
            h_text.set_position([var.Range[0] + 0.01 * np.diff(var.Range), 1.03])
        elif ext.x0 + np.diff([ext.x0, ext.x1]) > w_ext.x1:
            h_text.set_horizontalalignment('right')
            h_text.set_position([var.Range[1] - 0.01 * np.diff(var.Range), 1.03])
        
    plt.plot(x, y)

    if tex_out != '':
        import matplotlib2tikz

        if tex_out.endswith('.tex') is False:
            tex_out += '.tex'

        matplotlib2tikz.save(filepath=tex_out)

    if show:
        plt.show()
