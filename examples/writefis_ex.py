# https://www.mathworks.com/help/fuzzy/mamfis.writefis.html

import fuzzylab as fl

fis = fl.mamfis('tipper')
fis.addInput([0, 10], Name='service')
fis.addMF('service', 'gaussmf', [1.5, 0],Name='poor')
fis.addMF('service', 'gaussmf', [1.5, 5],Name='good')
fis.addMF('service', 'gaussmf', [1.5, 10],Name='excellent')

fl.writeFIS(fis, 'myFile')
