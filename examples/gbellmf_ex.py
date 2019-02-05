from matplotlib.pyplot import plot, xlabel, show
from fuzzylab import linspace, gbellmf

x = linspace(0, 0.1, 10)
y = gbellmf(x, [2, 4, 6])
plot(x, y)
xlabel('gbellmf, P = [2, 4, 6]')
show()
