import numpy as np

def gbellmf(x, params):
    
    assert len(params) == 3, 'Generalized membership function must have three parameters.'

    a, b, c = params

    if type(x) is not np.ndarray:
        x = np.asarray([x])

    return 1 / (1 + np.power(np.abs((x - c) / a), (2 * b)))
