% https://www.mathworks.com/help/fuzzy/defuzz.html

x = -10:0.1:10;
mf = trapmf(x,[-10 -8 -4 7]);
out = defuzz(x,mf,'centroid')
