# arange.py
# Eduardo Avelar
# August 2022

import numpy as np

def arange(start, step, stop):
    return np.linspace(start, stop, int(abs(stop - start) / step) + 1)
