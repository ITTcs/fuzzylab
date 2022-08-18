# https://www.mathworks.com/help/fuzzy/plotmf.html

import fuzzylab as fl

fis = fl.readfis('tipper')
fl.plotmf(fis,'input', 1)
