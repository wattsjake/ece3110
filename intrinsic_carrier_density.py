"""
created: 09 Sept 2021

Intrinsic carrier density
"""
import numpy as np

def intrinsic():
    B=1.08e31
    T=300
    Eg=1.12
    k=8.62e-5

    return (B*(T**3))*np.exp(-Eg/(k*T))


print(intrinsic[1])

ni2=intrinsic()
ni=np.sqrt(intrinsic())


print("==========Intrinsic Carrier Density==========")
print("B: %.3e" %B)
print("ni2:", "{:.2E}".format(ni2), "ni:", "{:.2E}".format(ni))
