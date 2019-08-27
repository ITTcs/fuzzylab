import numpy as np

def gaussmf2(x, params):
    
    assert len(params) == 3, 'Generalized membership function must have three parameters.'

    sig1,sig2, c = np.asarray(params)

    r1 = np.exp(-pow((x - c), 2) / (2 * pow(sig1, 2)))
    r2 = np.exp(-pow((x - c), 2) / (2 * pow(sig2, 2)))

    return r1, r2
