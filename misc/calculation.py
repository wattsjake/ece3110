"""
Created on 07 Sept 2021

Jacob Watts
"""

import numpy as np
import scipy.optimize

def ni(T):
    k=8.62e-5
    B=1.08e31
    Eg=1.12
    return np.sqrt(B*(T**3)*np.exp(-Eg/k/T))

def f(T):
    return ni(T)-2.31e19

x=scipy.optimize.brentq(f,1,4000)

print("At ", x, " Deg K, ni=", "{:.2E}".format(ni(x)))
