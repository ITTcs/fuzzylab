% https://www.mathworks.com/help/fuzzy/mamfis.writefis.html

fis = mamfis('Name','tipper');
fis = addInput(fis,[0 10],'Name','service');
fis = addMF(fis,'service','gaussmf',[1.5 0],'Name','poor');
fis = addMF(fis,'service','gaussmf',[1.5 5],'Name','good');
fis = addMF(fis,'service','gaussmf',[1.5 10],'Name','excellent');

writeFIS(fis,'myFile_mat');
