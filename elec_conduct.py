#electrical conductivity:

print("This program will help you find the electrical conductivity.\n"
    "You will need to know the electron and hole mobility.")

q = 1.601e-19


def sigma(mu_n, mu_p, n, p):
    sigma = q*(n*mu_n + p*mu_p)
    return sigma

def resistivity(sigma):
    rho = 1/sigma
    return rho

mu_n = float(input("Enter mu_n: "))
mu_p = float(input("Enter mu_p: "))
n = float(input("Enter n - electron concentration: "))
p = float(input("Enter p - hole concentration: "))


sigma = sigma(mu_n, mu_p, n, p)
rho = resistivity(sigma)

print("Sigma = %.2e    Rho = %.2e" %(sigma, rho))
