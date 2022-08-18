# https://www.mathworks.com/help/fuzzy/gbellmf.html

import matplotlib.pyplot as plt
import fuzzylab as fl

x = fl.arange(0, 0.1, 10)
y = fl.gbellmf(x, [2, 4, 6])

plt.plot(x, y)
plt.title('gbellmf, P=[2, 4, 6]')
plt.xlabel('x')
plt.ylabel('Degree of Membership')
plt.ylim([-0.05, 1.05])
plt.show()
