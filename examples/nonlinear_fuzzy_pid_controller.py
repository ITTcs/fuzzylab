from fuzzylab import sugfis, linspace, evalfis
import numpy as np

# Construct the FIS

fis = sugfis()

# Define input E

fis.addInput([-10, 10], Name='E')
fis.addMF('E','gaussmf',[7, -10],Name='Negative')
fis.addMF('E','gaussmf',[7, 10],Name='Positive')

# Define input CE

fis.addInput([-10, 10], Name='CE')
fis.addMF('CE','gaussmf',[7, -10],Name='Negative')
fis.addMF('CE','gaussmf',[7, 10],Name='Positive')

# Define output u

fis.addOutput([-20, 20], Name='u')
fis.addMF('u','constant', -20, Name='Min')
fis.addMF('u','constant', 0, Name='Zero')
fis.addMF('u','constant', 20, Name='Max')

# Define the following fuzzy rules:

# 1 If E is negative and CE is negative, then u is -20.
# 2 If E is negative and CE is positive, then u is 0.
# 3 If E is positive and CE is negative, then u is 0.
# 4 If E is positive and CE is positive, then u is 20.

ruleList = [[0, 0, 0, 1, 1], # Rule 1
            [0, 1, 1, 1, 1], # Rule 2
            [1, 0, 1, 1, 1], # Rule 3
            [1, 1, 2, 1, 1]] # Rule 4

fis.addRule(ruleList)

Step = 1
E = linspace(-10, Step, 10)
CE = linspace(-10, Step, 10)
N = len(E)

LookUpTableData = np.zeros((N, N))

for i in range(N):
    for j in range(N):
        # Compute output u for each combination of sample points.
        LookUpTableData[i,j] = evalfis(fis,[E[i], CE[j]])

print(LookUpTableData)
