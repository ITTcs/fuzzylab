import numpy as np

def gaussmf(x, params):
    
    assert len(params) == 2, 'Generalized membership function must have two parameters.'

    sig, c = np.asarray(params)

    return np.exp(-pow((x - c), 2) / (2 * pow(sig, 2)))
