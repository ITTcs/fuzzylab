# linspace.py
# Eduardo Avelar
# October 2018

import numpy as np

def linspace(start, step, stop):
    return np.linspace(start, stop, (abs(stop - start) / step) + 1)
