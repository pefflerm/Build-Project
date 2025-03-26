import time
import numpy as np
from matplotlib import pylab as plt
from matplotlib import animation as ani
import cProfile

START = time.time()

Jc = np.log(1+np.sqrt(2.))/2

Lx, Ly = 20, 20

J = 1. * Jc
U = -0.0

sigma = np.ones((Lx, Ly), dtype='i4')

#plt.imshow(sigma, vmin = -1, vmax = 1)
#plt.show()

def energy(sigma):
    en = 0

    # horizontal bonds
    for i in np.arange(Lx-1):
        for j in np.arange(Ly):
            en += -J*sigma[i,j]*sigma[i+1,j]

    # vertical bonds
    for i in np.arange(Lx):
        for j in np.arange(Ly-1):
            en += -J*sigma[i,j]*sigma[i,j+1]

    # external field
    for i in np.arange(Lx):
        for j in np.arange(Ly):
            en += -U*sigma[i,j]

    return en



# vectorize any for loops
def energy_vec(sigma):
    return (-J*np.sum(sigma[:-1,:]*sigma[1:,:])
            + -J*np.sum(sigma[:,:-1]*sigma[:,1:])
            + -U*np.sum(sigma))

#energy_vec(sigma)
#energy(sigma)

#END = time.time()

#print(f"{(END-START):.3f}s elapsed.")


def flip(sigma):
    """Loop through sites and randomly flip with probability 
    set by the relative statistical weight."""

    e0 = energy_vec(sigma)

    for i in np.arange(Lx):
        for j in np.arange(Ly):
            # propose a flip
            sigma[i,j]*= -1
            e1 = energy(sigma)
            deltaE = e1 - e0
            p = np.exp(- deltaE)/(np.exp(-deltaE)+np.exp(deltaE))

            if np.random.rand() < p:
                #accept flip and new energy
                d0 = e1
            else:
                #reject flip
                sigma[i,j]*=-1

    return 

def flip_local(sigma):
    for i in np.arange(Lx):
        for j in np.arange(Ly):
            localU = U

            if i < Lx-1:
                localU += J*sigma[i+1,j]
            if i > 0:
                localU += J*sigma[i-1,j]
            if j < Ly-1:
                localU += J*sigma[i,j+1]
            if j > 0:
                localU += J*sigma[i, j-1]
            # sample a spin configuration
            m = np.tanh(localU)
            p = (m+1)/2

            sigma[i,j] = 2*(np.random.rand()<p) -1
    return 




#cProfile.run('flip(sigma)')
#cProfile.run('flip_local(sigma)')


fig, ax = plt.subplots()
im = plt.imshow(sigma, vmin = -1, vmax = 1)

def animate(i):
    """Take a flip step and update image."""
    flip(sigma)
    im.set_data(sigma)
    return

Ani = ani.FuncAnimation(fig, animate, frames = 1000, interval = 0.1)
plt.show()
       
