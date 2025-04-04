# Explore Quantum Frontiers: Calculating Atoms 
This repository is for the 2025 February Build Project through Open Avenues. This project introduces key ideas from quantum physics to solve for to solve for a one-dimensional Ising model with an arbitrary number of atoms. Additionally, this project seeks to determine the relationship between the number of atoms and the run time to calculate the Hamiltonian.

## Requirements
This project requires the following Python packages:

* NumPy
* matplotlib
* time
* Cprofile

## Background: Understanding the 1D Ising model

## Usage
The file `Ising_chain_N` computes the Hamiltonian and eigenvalues for N atoms.

The number of atoms is set to 10, but can be adjusted at line 69.

Additionally, this file contains code to plot the energy levels as B and J change.


The file `Ising_chain_N_timePlot` computes the run time for calculating the Hamiltonian for various values of N. The resulting times are plotted as N increases.

The range of N is set to [3,12] but can be adjusted at line 62.

## Results
![Run Time versus Number of Atoms](/assets/images/RunTime_versus_N.png)