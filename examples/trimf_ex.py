# https://www.mathworks.com/help/fuzzy/trimf.html

import fuzzylab as fl
import matplotlib.pyplot as plt

x = fl.arange(0, 0.1, 10)
y = fl.trimf(x, [3, 6, 8])

plt.plot(x,y)
plt.title('trimf, P = [3, 6, 8]')
plt.xlabel('x')
plt.ylabel('Degree of Membership')
plt.ylim([-0.05, 1.05])
plt.show()
