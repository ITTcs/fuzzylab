import breaking_fis as bf
from fuzzylab import evalfis

# return output
y = evalfis(bf.fis, 0.12)
print(y)

# return output and rule firing strength
y, rule_firing = evalfis(bf.fis, 0.12, rule_firing=True)
print(rule_firing)
