from scipy import optimize

def f_up(Nt):
  return 44.9+426/(1+(Nt/2.23e16)**0.72)

def f_un(Nt):
    return 52.2+1365/(1+(Nt/9.68e16)**0.68)

def f_Na(Na, *params):
    rho=params[0]
    return rho*q*f_up(Na)*Na-1

def p23():
    Na1 = optimize.brentq(f_Na, 1e14, 1e17, args=1)
    Na2 = optimize.brentq(f_Na, 1e14, 1e18, args=0.18)
    print("Na1=","{:.3e}".format(Na1), " Na2=", "{:.3e}".format(Na2),\
        " Diff= ", "{:.3e}".format(Na2-Na1))
    print("u_p1=", "{:.3e}".format(f_up(Na1)), " up_2=",\
        "{:.3f}".format(f_up(Na2)))
    return

p23()
