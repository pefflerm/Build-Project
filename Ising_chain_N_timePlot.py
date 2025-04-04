import numpy as np
from matplotlib import pyplot as plt
from numpy import linalg as la
import time

########### Hamiltonian calculation from Ising_chain_N
Sx = np.array([[0,1.0],[1,0]])
Sy = np.array([[0,-1.j],[1.j,0]])
Sz = np.array([[1,0],[0,-1.0]])
Id = np.eye(2)
J = 1.0
B = 1.0
x = B/J
def calculateH(N):
    H1 = calculateSubH(N,True)
    H2 = calculateSubH(N,False)
    H = -H1 - x*H2
    return H
def calculateSubH(N, isH1):
    H = np.zeros((2**N,2**N))
    for i in range(1,N+1):
        H = np.add(H,calculateHTerm(N,i,isH1))
    return H
def calculateHTerm(N,i,isH1):
    list1 = generateList(N,i)
    dict = generateDict(N,list1,isH1)
    x = 3
    term = np.kron(dict.get(1),dict.get(2))
    while (x<=N):
        term = np.kron(term,dict.get(x))
        x += 1
    return term
def generateList(N,i):
    list1 = []
    for x in range(i,N+i):
        if (x>N):
            list1.append(x-N)
        else:
            list1.append(x)
    return list1
def generateDict(N,list1,isH1):
    dict = {}
    if (isH1):
        for x in range(N):
            if (x==0 or x==1):
                dict[list1[x]] = Sz
            else:
                dict[list1[x]] = Id
        return dict
    else:
        for x in range(N):
            if (x==0):
                dict[list1[x]] = Sx
            else:
                dict[list1[x]] = Id
        return dict
###########


########### Calculate run time for N = [3,12]
timeDiff = []
for x in range(3,13):
    start = time.time()
    H = calculateH(x)
    end = time.time()
    timeDiff.append((end-start))
print(timeDiff)
###########


########### Plot results
xValues = [3,4,5,6,7,8,9,10,11,12]
plt.plot(xValues, timeDiff,'o')
plt.xlabel("Number of atoms")
plt.ylabel("Run time (s)")
plt.show()
###########

