from matplotlib.pyplot import plot, xlabel, show
from fuzzylab import linspace, gaussmf

x = linspace(0, 0.1, 10)
y = gaussmf(x, [2, 5])
plot(x, y)
xlabel('gaussmf, P=[2, 5]')
show()
