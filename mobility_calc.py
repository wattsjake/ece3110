import numpy as np

def mobility_n(n_t):

    bottom = (1+(n_t/9.68e16)**0.68)
    mu_n = 52.2 + 1365/bottom

    return mu_n

def mobility_p(n_t):

    bottom = (1+(n_t/2.23e16)**0.72)
    mu_p = 44.9 + 426/bottom

    return mu_p

n_t = float(input("What is the N_T: "))

mu_n = mobility_n(n_t)
mu_p = mobility_p(n_t)

print("electron mobility - mu_n: %f\nhole mobility - mu_p: %f" %(mu_n, mu_p))
