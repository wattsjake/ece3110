#junction potential
import numpy as np

print("This program will help you find the juction potential.")

k = 1.38e-23
q = 1.6e-19
e = 8.85e-14

def junction(N_A, N_D, v_t, ni):
    theta = v_t*np.log((N_A*N_D)/ni**2)
    return theta

def thermal_volt(T):
    v_t = (k*T)/q
    return v_t

def depletion_region_with():
    print("hello")

T = float(input("Please enter temp in K: "))
v_t = thermal_volt(T)
N_A = float(input("Please enter the N_A: "))
N_D = float(input("Please enter the N_D: "))
ni = float(input("Please enter the ni: "))

theta = junction(N_A, N_D, v_t, ni)

print("v_t = %.4e V at %.2f" %(v_t, T))
print("Junction Potential(built-in potential): %.4eV" %theta)

cont = input("Would you like to know depletion-region width? y/n: ")

if cont == "y":

    #x_n = input("What is x_n: ")
    #x_p = input("What is x_p: ")

    w_do = np.sqrt(((2*11.7*e)/q)*((1/N_A)+(1/N_D))*theta)

    print("w_do: %.3e" %w_do)
