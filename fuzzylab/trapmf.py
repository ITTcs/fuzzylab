# trapmf.py
# Eduardo Avelar
# August 2022

import numpy as np

def trapmf(x, params):
    """
    Trapezoidal membership function generator.

    Parameters
    ----------
    x : 1d array
        Independent variable.
    params : 1d array, length 4
        Four-element vector.  Ensure a <= b <= c <= d.

    Returns
    -------
    y : 1d array
        Trapezoidal membership function.
    """
    assert len(params) == 4, 'Trapezoidal membership function must have four parameters.'
    
    a, b, c, d = params
    assert a <= b, 'First parameter must be less than or equal to second parameter.'
    assert b <= c, 'Second parameter must be less than or equal to third parameter.'
    assert c <= d, 'Third parameter must be less than or equal to fourth parameter.'

    if type(x) is not np.ndarray:
        x = np.asarray([x])

    y = np.zeros(len(x))

    # Left slope
    if a != b:
        index = np.logical_and(a < x, x < b)
        y[index] = (x[index] - a) / (b - a)
        
    # Right slope
    if c != d:    
        index = np.logical_and(c < x, x < d)            
        y[index] = (d - x[index]) / (d - c)

    # Top
    index = np.logical_and(b <= x, x <= c)           
    y[index] = 1

    return y