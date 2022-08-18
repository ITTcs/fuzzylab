# defuzz.py
# Eduardo Avelar
# August 2022

import numpy as np

def defuzz(x, y, defuzz_method):
    
    if defuzz_method == 'centroid':
        total_area = sum(y)
        return sum(y * x) / total_area
    elif defuzz_method == 'bisector':
        total_area = sum(y)
        data_n = len(x)
        tmp = y[0]
        for k in range(1, data_n):
            tmp = tmp + y[k]
            if tmp >= total_area/2:
                break
        return x[k]
    elif defuzz_method == 'mom':
        return np.mean(x[y == max(y)])
    elif defuzz_method == 'som':
        tmp = x[y == max(y)]
        which = np.argmin(abs(tmp))
        return tmp[which]
    elif defuzz_method == 'lom':
        tmp = x[y == max(y)]
        which = np.argmax(abs(tmp))
        return tmp[which]
    elif defuzz_method == 'wtaver':
        return sum(x * y) / sum (y)
    else:
        raise ValueError('The input for `type`, %s, was incorrect.' % (type))
    