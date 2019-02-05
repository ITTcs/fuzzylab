from matplotlib.pyplot import plot, xlabel, show
from fuzzylab import linspace, trimf

x = linspace(0, 0.1, 10)
y = trimf(x, [3, 6, 8])
plot(x, y)
xlabel('trimf, P = [3, 6, 8]')
show()
