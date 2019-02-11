import matplotlib.pyplot as plt
import numpy as np

from .trimf import trimf
from .gaussmf import gaussmf
from .trapmf import trapmf

def evalmf(mf, x):
    if mf.Type is 'trimf':
        return trimf(x, mf.Parameters)
    if mf.Type is 'trapmf':
        return trapmf(x, mf.Parameters)
    elif mf.Type is 'gaussmf':
        return gaussmf(x, mf.Parameters)