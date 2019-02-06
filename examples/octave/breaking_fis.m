pkg load fuzzy-logic-toolkit

fis = newfis ('breaking', 'sugeno', ...
            'algebraic_product', 'algebraic_sum', ...
            'min', 'max', 'wtaver');

fis = addvar (fis, 'input', 'distance', [0.12 3.5]);
fis = addmf (fis, 'input', 1, 'minimum', 'gaussmf', [0.31296 0.12]);
fis = addmf (fis, 'input', 1, 'short', 'gaussmf', [0.31296 1.2467]);
fis = addmf (fis, 'input', 1, 'medium', 'gaussmf', [0.31296 2.3733]);
fis = addmf (fis, 'input', 1, 'long', 'gaussmf', [0.31296 3.5]);

fis = addvar (fis, 'output', 'velocity', [0 2.22]);
fis = addmf (fis, 'output', 1, 'null', 'constant', 0);
fis = addmf (fis, 'output', 1, 'minimum', 'constant', 0.74);
fis = addmf (fis, 'output', 1, 'recommended', 'constant', 1.48);
fis = addmf (fis, 'output', 1, 'maximum', 'constant', 2.22);

ruleList = [1 1 1 1; ...    ## Rule 1
            2 2 1 1; ...    ## Rule 2
            3 3 1 1; ...    ## Rule 3
            4 4 1 1];       ## Rule 4

fis = addrule(fis, ruleList);

y = evalfis(0.12, fis)

plotmf(fis, 'input', 1);
gensurf(fis);

pause(3);