import scipy.sparse as sps
import numpy as np
from matplotlib import pyplot as plt

Id = np.eye(2)
Sx = np.array([[0,1.0],[1,0]])
Sz = np.array([[1,0.],[0,-1]])
Sy = -1j * np.matmul(Sz,Sx)

#rint(Sx)
#print(Sy)
#print(Sz)

S2 = np.kron(Sx, Id)
#print(S2)

S3 = np.kron(np.kron(Sx, Id),Id)
print(S3)

#plt.spy(S3)
#plt.show()


# diagnolization
(e, u) = np.linalg.eigh(S3)

print(e)
print(u)
