import matplotlib.pyplot as plt
import numpy as np

from .trimf import trimf
from .gaussmf import gaussmf
from .trapmf import trapmf

def evalmf(mf, x):
    
    if mf.Type == 'trimf':
        y = trimf(x, mf.Parameters)
    if mf.Type == 'trapmf':
        y = trapmf(x, mf.Parameters)
    elif mf.Type == 'gaussmf':
        y = gaussmf(x, mf.Parameters)

    return y