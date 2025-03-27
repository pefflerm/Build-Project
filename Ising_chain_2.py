# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 10:13:01 2025

@author: TengZhang
"""

import numpy as np
from matplotlib import pyplot as plt
import scipy
import time
from numpy import linalg as la

START = time.time()

########### Pauli matrices
Sx = np.array([[0,1.0],[1,0]])
Sy = np.array([[0,-1.j],[1.j,0]])
Sz = np.array([[1,0],[0,-1.0]])
Id = np.eye(2)

print(Sx)
print(Sy)
print(Sz)
print(Id)
###########


########### Set up spin Hamiltonians for 3 spins
J = 1.0
B = 1.0
x = B/J

H1 = np.kron(np.kron(Sz,Sz),Id)+np.kron(np.kron(Id,Sz),Sz)+np.kron(np.kron(Sz,Id),Sz)


H2 = np.kron(np.kron(Sx,Id),Id)+np.kron(np.kron(Id,Sx),Id)+np.kron(np.kron(Id,Id),Sx)

H = -H1 - x*H2

print(H)
###########


########### Solve for energy eigenvalues
eigenvalues, eigenvectors = la.eig(H)


print(eigenvalues)
###########


########### Vary relative strength of the 2 terms and plot the energy levels
N_point = 100
para_list = np.linspace(0,3,N_point)
Energy = []


for x0 in para_list:
    H = -H1 - x0*H2
    eigenvalues, eigenvectors = la.eig(H)
    Energy.append(np.real(eigenvalues))

plt.plot(para_list, np.array(Energy),'o')
plt.xlabel("B/J")
plt.ylabel("Energy")
plt.show()
##########



END = time.time()
print(f"Time elapsed is {(END-START):.15f}s")
