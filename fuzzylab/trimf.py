# trimf.py
# Eduardo Avelar
# August 2022

import numpy as np

def trimf(x, params):
    """
    Triangular membership function generator.

    Parameters
    ----------
    x : 1d array
        Independent variable.
    params : 1d array, length 3
        Three-element vector controlling shape of triangular function.
        Requires a <= b <= c.

    Returns
    -------
    y : 1d array
        Triangular membership function.
    """
    assert len(params) == 3, 'Triangular membership function must have three parameters.'

    a, b, c = params
    assert a <= b, 'First parameter must be less than or equal to second parameter.'
    assert b <= c, 'Second parameter must be less than or equal to third parameter.'

    if type(x) is not np.ndarray:
        x = np.asarray([x])

    y = np.zeros(len(x))
  
    # Left slope
    if a != b:
        index = np.logical_and(a < x, x < b)
        y[index] = (x[index] - a) / (b - a)

    # Right slope
    if b != c:    
        index = np.logical_and(b < x, x < c)              
        y[index] = (c - x[index]) / (c - b)

    # Center
    y[x == b] = 1
    
    return y
