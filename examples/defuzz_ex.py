# https://www.mathworks.com/help/fuzzy/defuzz.html

import fuzzylab as fl

x = fl.arange(-10, 0.1, 10)
mf = fl.trapmf(x, [-10, -8, -4, 7])
out = fl.defuzz(x, mf, 'centroid')
print(out)
