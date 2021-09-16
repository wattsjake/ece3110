import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
s = np.linspace(0, 10, int(10e3))
v = np.sin(s)*np.exp(-s)+0.4*np.sin(10*s)*np.exp(-s/2)+0.3*np.sin(200*s)*np.exp(-2*s)
#
plt.plot(s,v)
plt.title("hammer test")
plt.xlabel("Time(sec)")
plt.ylabel("Volts")
plt.show()
