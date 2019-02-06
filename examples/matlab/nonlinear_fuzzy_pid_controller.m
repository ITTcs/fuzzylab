% Construct the fis

fis = sugfis

% Define input E

fis = addInput(fis,[-10 10],'Name','E');
fis = addMF(fis,'E','gaussmf',[7 -10],'Name','Negative');
fis = addMF(fis,'E','gaussmf',[7 10],'Name','Positive');

% Define input CE

fis = addInput(fis,[-10 10],'Name','CE');
fis = addMF(fis,'CE','gaussmf',[7 -10],'Name','Negative');
fis = addMF(fis,'CE','gaussmf',[7 10],'Name','Positive');

% Define output u

fis = addOutput(fis,[-20 20],'Name','u');
fis = addMF(fis,'u','constant',-20,'Name','Min');
fis = addMF(fis,'u','constant',0,'Name','Zero');
fis = addMF(fis,'u','constant',20,'Name','Max');

% Define the following fuzzy rules:

% 1 If E is negative and CE is negative, then u is -20.
% 2 If E is negative and CE is positive, then u is 0.
% 3 If E is positive and CE is negative, then u is 0.
% 4 If E is positive and CE is positive, then u is 20.

ruleList = [1 1 1 1 1;  % Rule 1
            1 2 2 1 1;  % Rule 2
            2 1 2 1 1;  % Rule 3
            2 2 3 1 1]; % Rule 4

fis = addrule(fis, ruleList);

Step = 1;
E = -10:Step:10;
CE = -10:Step:10;
N = length(E);

LookUpTableData = zeros(N);

for i=1:N
    for j=1:N
        % Compute output u for each combination of sample points
        LookUpTableData(i,j) = evalfis([E(i) CE(j)], fis);
    end
end

LookUpTableData
