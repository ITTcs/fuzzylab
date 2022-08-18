# https://www.mathworks.com/help/fuzzy/gaussmf.html

import fuzzylab as fl
import matplotlib.pyplot as plt

x = fl.arange(0, 0.1, 10)
y = fl.gaussmf(x, [2, 5])

plt.plot(x, y)
plt.xlabel('gaussmf, P=[2, 5]')
plt.ylabel('Membership')
plt.ylim([-0.05, 1.05])
plt.show()
