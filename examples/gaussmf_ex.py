from matplotlib.pyplot import plot, xlabel, show
from fuzzylab import linspace, gaussmf2

x = linspace(0, 0.1, 10)
y1,y2 = gaussmf2(x, [1,2, 5])
plot(x,y1)
plot(x,y2)
xlabel('gaussmf2, P=[2, 5]')
show()
