fis = sugfis;

fis = addInput(fis, [0.12 3.5],'Name','distance');
fis = addMF(fis,'distance','gaussmf', [0.31296 0.1200],'Name','minimum');
fis = addMF(fis,'distance','gaussmf', [0.31296 1.2467],'Name','short');
fis = addMF(fis,'distance','gaussmf', [0.31296 2.3733],'Name','medium');
fis = addMF(fis,'distance','gaussmf', [0.31296 3.5000],'Name','long');

fis = addOutput(fis, [0 2.22],'Name', 'velocity');
fis = addMF(fis,'velocity','constant',0.00,'Name','null');
fis = addMF(fis,'velocity','constant',0.74,'Name','minimum');
fis = addMF(fis,'velocity','constant',1.48,'Name','recommended');
fis = addMF(fis,'velocity','constant',2.22,'Name','maximum');

% If distance is minimum then velocity null
% If distance is short then velocity minimum
% If distance is medium then velocity recommended
% If distance is long then velocity maximum

ruleList = [1 1 1 1;    % Rule 1
            2 2 1 1;    % Rule 2
            3 3 1 1;    % Rule 3
            4 4 1 1];   % Rule 4

fis = addRule(fis, ruleList);
