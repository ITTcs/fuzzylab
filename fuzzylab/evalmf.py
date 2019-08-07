import matplotlib.pyplot as plt
import numpy as np

from .trimf import trimf
from .gaussmf import gaussmf
from .trapmf import trapmf

def evalmf(mf, x):
    if mf.Type == 'trimf':
        return trimf(x, mf.Parameters)
    if mf.Type == 'trapmf':
        return trapmf(x, mf.Parameters)
    elif mf.Type == 'gaussmf':
        return gaussmf(x, mf.Parameters)