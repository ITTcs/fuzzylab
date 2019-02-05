import numpy as np
from matplotlib.pyplot import plot, ylim, show, vlines, text
from fuzzylab import linspace, trapmf, defuzz

x = linspace(-10, 0.1, 10)

mf1 = trapmf(x,[-10, -8, -2, 2])
mf2 = trapmf(x,[-5, -3, 2, 4])
mf3 = trapmf(x,[2, 3, 8, 9])
mf1 = np.fmax(0.5 * mf2, np.fmax(0.9 * mf1, 0.1 * mf3))

x1 = defuzz(x, mf1, 'centroid')
x2 = defuzz(x, mf1, 'bisector')
x3 = defuzz(x, mf1, 'mom')
x4 = defuzz(x, mf1, 'som')
x5 = defuzz(x, mf1, 'lom')

gray = [x*0.7 for x in [1, 1, 1]]

vlines(x1, -0.2, 1, color='r')
text(x1, -0.24, ' centroid', fontweight='bold', color='r')
vlines(x2, -0.4, 1, color=gray)
text(x2, -0.44, ' bisector', fontweight='bold', color=gray)
vlines(x3, -0.7, 1, color=gray)
text(x3, -0.74, ' MOM', fontweight='bold', color=gray)
vlines(x4, -0.8, 1, color=gray)
text(x4, -0.84, ' SOM', fontweight='bold', color=gray)
vlines(x5, -0.6, 1, color=gray)
text(x5, -0.64, ' LOM', fontweight='bold', color=gray)

plot(x, mf1, lineWidth=3)
ylim(-1, 1)
show()