"""
Created on 07 Sept 2021

Jacob Watts
"""

import numpy as np
import scipy.optimize

def ni(T):
    k=8.62e-5
    B=1.03e31
    Eg=1.12
    return np.sqrt(B*(T**3)*np.exp(-Eg/k/T))

def f(T):
    return ni(T)-1e10

x=scipy.optimize.brentq(f,100,1000)

print("At ", x, " Deg K, ni=", "{:.2E}".format(ni(x)))
