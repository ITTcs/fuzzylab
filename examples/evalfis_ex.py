# https://www.mathworks.com/help/fuzzy/evalfis.html

import fuzzylab as fl

fis = fl.readfis('tipper')
output = fl.evalfis(fis, [2, 1])
print(output)
