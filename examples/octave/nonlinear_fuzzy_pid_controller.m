pkg load fuzzy-logic-toolkit

# Construct the FIS

fis = newfis ('breaking', 'sugeno', ...
            'algebraic_product', 'algebraic_sum', ...
            'min', 'sum', 'wtaver');

# Define input E

fis = addvar (fis, 'input', 'E', [-10 10]);
fis = addmf (fis, 'input', 1, 'Negative', 'gaussmf', [7 -10]);
fis = addmf (fis, 'input', 1, 'Positive', 'gaussmf', [7 10]);

# Define input CE

fis = addvar (fis, 'input', 'CE', [-10 10]);
fis = addmf (fis, 'input', 2, 'Negative', 'gaussmf', [7 -10]);
fis = addmf (fis, 'input', 2, 'Positive', 'gaussmf', [7 10]);

# Define output u

fis = addvar (fis, 'output', 'u', [-20 20]);
fis = addmf (fis, 'output', 1, 'Min', 'constant', -20);
fis = addmf (fis, 'output', 1, 'Zero', 'constant', 0);
fis = addmf (fis, 'output', 1, 'Max', 'constant', 20);

ruleList = [1 1 1 1 1; ...    # Rule 1
            1 2 2 1 1; ...    # Rule 2
            2 1 2 1 1; ...    # Rule 3
            2 2 3 1 1];       # Rule 4

fis = addrule(fis, ruleList);

step = 1;
E = -10:step:10;
CE = -10:step:10;
N = length(E);

LookUpTableData = zeros(N);

for i=1:N
    for j=1:N
        # Compute output u for each combination of sample points
        LookUpTableData(i,j) = evalfis([E(i) CE(j)], fis);
    end
end

LookUpTableData
