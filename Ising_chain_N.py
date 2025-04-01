# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 10:13:01 2025

@author: TengZhang
"""

import numpy as np
from matplotlib import pyplot as plt
import time
from numpy import linalg as la
from functools import reduce
from typing import Final

START = time.time()

########### Pauli matrices
########### Use all capitals, meaning it's constant
SX: Final = np.array([[0,1.0],[1,0]])
SY: Final = np.array([[0,-1.j],[1.j,0]])
SZ: Final = np.array([[1,0],[0,-1.0]])
ID: Final = np.eye(2)

#print(SX)
#print(SY)
#print(SZ)
#print(ID)

########### Helper functions to construct the Hamiltonian
def Construct_OpList_single(N: int, index: int):
    ################ This function constructs a list of Identity operators and a single SX operator at site i=index
    ################ Read and understand this function
    OpList = []
    for i in np.arange(N):
        if i == index:
            OpList.append(SX)
        else:
            OpList.append(ID)
    return OpList

def Construct_H2(N: int, B: float):
    ################ This function constructs the external B field Hamiltonian
    ################ Read and understand how reduce() works
    H2 = np.zeros((2**N,2**N))
    for i in np.arange(N):
        OpList = Construct_OpList_single(N, i)
        print(OpList)
        H2 += -B*reduce(np.kron, OpList)
    return H2

def Construct_OpList_double(N: int, index: int):
    ################ This function constructs a list of Identity operators and two SZ operator at site i=index and i+1
    ################ Read and understand this function
    OpList = []
    for i in np.arange(N):
        if i == index or i == index+1:
            OpList.append(SZ)
        else:
            OpList.append(ID)
    if index == N-1:
        ############ this condition handles the periodic boundary condition
        OpList[0] = SZ
    return OpList

def Construct_H1(N: int, J: float):
    ################ This function constructs the spin interaction Hamiltonian
    H1 = np.zeros((2**N,2**N))
    for i in np.arange(N):
        OpList = Construct_OpList_double(N, i)
        print(OpList)
        H1 += -J*reduce(np.kron, OpList)
    return H1




J = 1.0
B = 1.0
x = B/J
##################### Test case with N=3. Change this value to arbitrary integer
N = 3
H1 = Construct_H1(N, J)
H2 = Construct_H2(N, B)
H = H1 + x*H2

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
    H = H1 + x0*H2
    eigenvalues, eigenvectors = la.eig(H)
    Energy.append(np.real(eigenvalues))

plt.plot(para_list, np.array(Energy),'o')
plt.xlabel("B/J")
plt.ylabel("Energy")
##########



END = time.time()
print(f"Time elapsed is {(END-START):.15f}s")
