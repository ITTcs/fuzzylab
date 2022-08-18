import numpy as np

def gaussmf(x, params):
    
    assert len(params) == 2, 'Generalized membership function must have two parameters.'

    sig, c = params

    if type(x) is not np.ndarray:
        x = np.asarray([x])

    return np.exp(-np.power((x - c), 2) / (2 * np.power(sig, 2)))
