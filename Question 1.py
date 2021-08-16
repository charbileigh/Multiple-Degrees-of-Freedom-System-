# MEC4047F - Mechanical Vibrations: Project 2
# Project 2: Part 1 Question b and c
# Name: Francesca Seopa
# Student Number: SPXMMA001


'''
    The purpose of this project is to calculate the eigen values and
    The eigen vectors of the first part of the project. These eigen values
    and eigen vectors will be used to calculate the modal frequencies and modal
    shapes for the model.

'''


#Importing the numpy library
import numpy as np
import math as sqrt

#Creating the K value matrix
kmatrix = np.array([[2831.3172, -2831.3172,0],[-2831.3172, 5987.594, -5037.903],[0, -5037.903,8041.269]]);

#Creating the i value matrix
imatrix = np.array([[0.1728,0,0],[0,7.03e-3, 0],[0,0,0.2048]]);

#finding the eigen vectors and eigen values for the k matrix
k_eigenValues, k_eigenVectors = np.linalg.eig(kmatrix);

#finding the eigen vectors and eigen values for the i matrix
i_eigenValues, i_eigenVectors = np.linalg.eig(imatrix);
print()
print()



#Printing the eigen values of the k matrix
print("Printing the Eigen values of the given k matrix array:\n",
      k_eigenValues)
print()
print()

#Prining the eigen vectors of the k matrix
print("Printing Right eigenvectors of the given k matrix array:\n",
      k_eigenVectors)
print()
print()

#Prinitng the K frequencies
k_frequencies = np.sqrt(k_eigenValues)
print("K frequency values:\n",k_frequencies)
print()
print()

#finding the eigen vectors and eigen values for the i matrix
i_eigenValues, i_eigenVectors = np.linalg.eig(imatrix)
print()
print()

#Printing the eigen values of the i matrix
print("Printing the Eigen values of the given i matrix array:\n",
      i_eigenValues)
print()
print()

#Prining the eigen vectors of the i matrix
print("Printing Right eigenvectors of the given i matrix array:\n",
      i_eigenVectors)
print()
print()

#printing the i frequencies
i_frequencies = np.sqrt(i_eigenValues)
print("I frequency values:\n",i_frequencies)
print()
print()


