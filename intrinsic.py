import numpy as np
import sys

def intrinsic(T):
    B=1.08e31
    Eg=1.12
    k=8.62e-5

    return (B*(T**3))*np.exp(-Eg/(k*T))

print("==========Intrinsic Carrier Density==========")
print("This program will find the intrinsic carrier density of Silicon\n"
      "at a certain K. Please enter the temperature value in K.\n")

#change input to float
T = float(input())

#call the intrinstic function and put T inside of it
ni2=intrinsic(T)
ni=np.sqrt(intrinsic(T))

#print out the results
print("ni2:", "{:.2E}".format(ni2), "ni:", "{:.2E}".format(ni))
