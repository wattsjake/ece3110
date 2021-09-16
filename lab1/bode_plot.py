import scipy
import numpy as np
import matplotlib.pyplot as plt

freq = []
V_R = []
V_IN = []
delta_t = []

ratio = []
phase = []
dB = []

with open("freq_hw1.txt", "r") as file:
    for line in file:
        freq.append(float(line))

with open("V_R_hw1.txt", "r") as file:
    for line in file:
        V_R.append(line)

with open("V_IN_hw1.txt", "r") as file:
    for line in file:
        V_IN.append(line)

with open("delta_t.txt", "r") as file:
    for line in file:
        delta_t.append(line)


#calcualte the dB
for i in range(len(V_R)):
    Vin = float(V_IN[i])
    Vout = float(V_R[i])

    ratio.append(Vout/Vin)

for item in ratio:
    dB.append(20*np.log(item))

#calculate the phase
for i in range(len(delta_t)):
    phase.append((float(delta_t[i])*1e-6)*(float(freq[i])*1e3)*360)


plt.plot(freq, dB)
plt.xscale("log")
plt.title("Freqency Response")
plt.xlabel("kHz")
plt.ylabel("dB")
plt.show()

plt.plot(freq, phase)
plt.xscale("log")
plt.title("Phase")
plt.xlabel("kHz")
plt.ylabel("degrees")
plt.show()
