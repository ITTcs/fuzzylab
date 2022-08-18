import fuzzylab as fl
import numpy as np

# Construct the fuzzy inference system

fis = fl.sugfis()

# Define input variable E

fis.addInput([-10, 10], Name='E')
fis.addMF('E','trimf',[-20, -10, 0],Name='Negative')
fis.addMF('E','trimf',[-10, 0, 10],Name='Zero')
fis.addMF('E','trimf',[0, 10, 20],Name='Positive')

# Define input CE.

fis.addInput([-10, 10], Name='CE')
fis.addMF('CE','trimf',[-20, -10, 0],Name='Negative')
fis.addMF('CE','trimf',[-10, 0, 10],Name='Zero')
fis.addMF('CE','trimf',[0, 10, 20],Name='Positive')

# Define output variable u with constant membership functions

fis.addOutput([-20, 20], Name='u')
fis.addMF('u','constant', -20, Name='LargeNegative')
fis.addMF('u','constant', -10, Name='SmallNegative')
fis.addMF('u','constant', 0, Name='Zero')
fis.addMF('u','constant', 10, Name='SmallPositive')
fis.addMF('u','constant', 20, Name='LargePositive')

# Define the following fuzzy rules:

# 1 If E is negative and CE is negative, then u is -20.
# 2 If E is negative and CE is zero, then u is -10.
# 3 If E is negative and CE is positive then u is 0.
# 4 If E is zero and CE is negative, then u is -10.
# 5 If E is zero and CE is zero, then u is 0.
# 6 If E is zero and CE is positive, then u is 10.
# 7 If E is positive and CE is negative, then u is 0.
# 8 If E is positive and CE is zero, then u is 10.
# 9 If E is positive and CE is positive, then u is 20.

ruleList = [[1, 1, 1, 1, 1], # Rule 1
            [1, 2, 2, 1, 1], # Rule 2
            [1, 3, 3, 1, 1], # Rule 3
            [2, 1, 2, 1, 1], # Rule 4
            [2, 2, 3, 1, 1], # Rule 5
            [2, 3, 4, 1, 1], # Rule 6
            [3, 1, 3, 1, 1], # Rule 7
            [3, 2, 4, 1, 1], # Rule 8
            [3, 3, 5, 1, 1]] # Rule 9

fis.addRule(ruleList)

Step = 10
E = fl.arange(-10, Step, 10)
CE = fl.arange(-10, Step, 10)
N = len(E)

LookUpTableData = np.zeros((N, N))

for i in range(N):
    for j in range(N):
        # Compute output u for each combination of sample points.
        LookUpTableData[i,j] = fl.evalfis(fis,[E[i], CE[j]])

print(LookUpTableData)
