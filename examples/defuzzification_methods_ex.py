# https://www.mathworks.com/help/fuzzy/defuzzification-methods.html

import fuzzylab as fl
import matplotlib.pyplot as plt
import numpy as np

x = fl.arange(0, 0.1, 20)

mf1 = fl.trapmf(x, [0, 2, 8, 12])
mf2 = fl.trapmf(x, [5, 7, 12, 14])
mf3 = fl.trapmf(x, [12, 13, 18, 19])
mf = np.maximum(0.5 * mf2, np.maximum(0.9 * mf1, 0.1 * mf3))

plt.plot(x, mf, linewidth=3)
plt.ylim(-1, 1)

xCentroid = fl.defuzz(x, mf, 'centroid')
xBisector = fl.defuzz(x, mf, 'bisector')
xMOM = fl.defuzz(x, mf, 'mom')
xSOM = fl.defuzz(x, mf, 'som')
xLOM = fl.defuzz(x, mf, 'lom')

gray = [x*0.7 for x in [1, 1, 1]]

plt.vlines(xCentroid, -0.2, 1.2, color='r')
plt.text(xCentroid, -0.2, ' centroid', fontweight='bold', color='r')
plt.vlines(xBisector, -0.4, 1.2, color=gray)
plt.text(xBisector, -0.4, ' bisector', fontweight='bold', color=gray)
plt.vlines(xMOM, -0.7, 1.2, color=gray)
plt.text(xMOM, -0.7, ' MOM', fontweight='bold', color=gray)
plt.vlines(xSOM, -0.7, 1.2, color=gray)
plt.text(xSOM, -0.7, ' SOM', fontweight='bold', color=gray)
plt.vlines(xLOM, -0.7, 1.2, color=gray)
plt.text(xLOM, -0.7, ' LOM', fontweight='bold', color=gray)

plt.show()
