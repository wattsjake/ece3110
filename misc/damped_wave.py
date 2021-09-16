import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.linspace(0, 10, int(10e5))
v = np.exp(-t)*np.sin(2*np.pi*t)

plt.plot(t,v)
plt.title("damped sine wave")
plt.xlabel("Time(s)")
plt.ylabel("Units")
plt.show()
