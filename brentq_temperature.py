import numpy as np
import scipy.optimize
import sys


def f_ni(T):
    return np.sqrt(B*T**3*np.exp(-Eg/(k*T)))

def n(T, *params):
    return f_ni(T)-params[0] #-1e12 is the ni that you want to find out.

T=scipy.optimize.brentq(n,30,700, args=1e2)

print("{:.2E}".format(T), "{:.2E}".format(f_ni(T)))
