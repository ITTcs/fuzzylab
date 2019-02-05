from fuzzylab import linspace, trapmf, defuzz

x = linspace(-10, 0.1, 10)
mf = trapmf(x, [-10, -8, -4, 7])
out = defuzz(x, mf, 'centroid')
print(out)
