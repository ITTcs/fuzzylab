import numpy as np

def gbellmf(x, params):
    
    assert len(params) == 3, 'Generalized membership function must have three parameters.'

    a, b, c = np.asarray(params)

    return 1 / (1 + pow(abs((x - c) / a), (2 * b)))
