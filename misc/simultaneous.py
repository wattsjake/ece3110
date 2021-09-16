import sympy as sym
import numpy as np

VDD=3.3
Vto=0.6
VH=VDD
R=75000
K=80e-6
WL=2
gamma=0.5
phi=0.3

VL, Id = sym.symbols('VL Id')
solution = sym.solve((VDD-Id*R-))

#equations should be in the form of equal to zero(0)
