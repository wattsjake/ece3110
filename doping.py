#doping levels
import numpy as np

print("This program will help you find the n-electron concentration\n"
    "and the p - hole concentration. You need to enter the values of the\n"
    "doped silicon.")

#instrinsic silicon at 300K
ni = 10**10

#type
type = "none"

#for n type semiconductor
def n_type(N_A, N_D):
    n = (N_D - N_A)
    p = (ni**2)/n

    return n,p

#for p type semiconductor
def p_type(N_A, N_D):
    p = (N_A - N_D)
    n = (ni**2)/p

    return n,p

def ni_2(p,n):
    ni = np.sqrt(p*n)
    ni_2 = p*n

    return ni,ni_2

N_A = float(input("Enter N_A: "))
N_D = float(input("Enter N_D: "))

#formula for p-type
if(N_A > N_D):
    (n,p) = p_type(N_A, N_D)
    type = "p"
else:
    (n,p) = n_type(N_A, N_D)
    type = "n"

(ni,ni_2) = ni_2(p,n)

print("%s-type n=%.2e p=%.2e" %(type, n, p))
print("ni: %.2e     ni_2: %.2e" %(ni, ni_2))
