# Name + Surname: Francesca Seopa
# Student Number: SPXMMA001
# MEC4047F - Resubmission of GA For Assignment 2

#--------------------------------------------------------


''' 
    The prupose of this project is to calculate the eigenvalues + eigenvectors
    of the first part of the project. These eiegn values and eigen vectors will 
    be used to calculate the modal frequencies and shapes of the model

'''


# initializing the libraries that will be used in calculating the
# eigen vectors and eigen values to get the natural frequencies + modes
import numpy as np
import math
from scipy.linalg import eigh
#--------------------------------------------------------


# The parameters listed below are the material properties 
# given for the project
E = 200E9           # Pa
v = 0.3             # Poisson's ratio
G = E/(2*(1+v))     # Pa
PI    = math.pi
OMEGA = 5.0          # radians / sec - frequency of forcing function]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# printing the G value after calculation
print("-----------------------------")
print()
print("G = {} Pa".format(G))
print()
print("-----------------------------")
#--------------------------------------------------------

# initialising the masses for the different DOFs 
MASS_1 = 12.0           # mass 1 (kg)
MASS_2 = 1.0            # mass 2 (kg)
MASS_3 = 1.6            # mass 3 (kg)
MASS_4 = 8.0            # mass 4 (kg)

# initialising the masses for the gear + motor connections
INPUT_MASS_12          = 0.7           # input mass (kg)
OUTPUT_MASS_34         = 1.7           # output mass (kg)
INPUT_SHAFT_LENGTH_12  = 280E-3        # input length (m) 
OUTPUT_SHAFT_LENGTH_34 = 220E-3        # input length (m)

# initialising the diameters for the masses
MASS_DIAMETER_1 = 240E-3         # mass 1 diameter
MASS_DIAMETER_2 = 104E-3         # mass 2 diameter
MASS_DIAMETER_3 = 166E-3         # mass 3 diameter
MASS_DIAMETER_4 = 320E-3         # mass 4 diameter

# initialising the diameters of the connecting shafts
INPUT_SHAFT_DIAMETER_12  = 18E-3         # input shaft diameter
OUTPUT_SHAFT_DIAMETER_34 = 22E-3         # output shaft diameter

# gear ratio and the damping coefficient
GEAR_RATIO = MASS_DIAMETER_2/MASS_DIAMETER_3
Ceq = 0.05         # damping coefficient (N.s/m)


#--------------------------------------------------------

# calculations for the moment of inertia for all bodies in (m^4)
MASS_1_INERTIA  = (1/8) * MASS_1 * MASS_DIAMETER_1 ** 2
MASS_2_INERTIA  = (1/8) * MASS_2 * MASS_DIAMETER_2 ** 2
MASS_3_INERTIA  = (1/8) * MASS_3 * MASS_DIAMETER_3 ** 2
MASS_4_INERTIA  = (1/4) * MASS_4 * MASS_DIAMETER_4 ** 2
j12 = (PI * INPUT_SHAFT_DIAMETER_12 ** 4)/32
j34 = (PI * OUTPUT_SHAFT_DIAMETER_34 ** 4)/32


# Printing the values that were calculated above of the inertia
print("I1 = {} kgm^2".format(MASS_1_INERTIA))
print()
print("I2 = {} kgm^2".format(MASS_2_INERTIA))
print()
print("I3 = {} kgm^2".format(MASS_3_INERTIA))
print()
print("I4 = {} kgm^2".format(MASS_4_INERTIA))
print()
print("-----------------------------")

#--------------------------------------------------------

# calculating the spring constants and declaring the number of DOFs
k1        = G * j12/INPUT_SHAFT_DIAMETER_12       # spring constant (N/m)
k2        = G * j34/OUTPUT_SHAFT_LENGTH_34        # spring constant (N/m)
time_step = 1.0e-4
end_time  = 10.0
dof       = 3               # Number of Degrees of Freedom 

# printing the spring constants that were calculated above
print()
print("k1 = {} Nm".format(k1))
print()
print("k2 = {} Nm".format(k2))
print()
print("------------------")


#--------------------------------------------------------


# setting up the matrices of the EOM to further calculate for 
# eigenvalues and eigenvectors [natural frequencies + modes]
M = np.array([[MASS_1_INERTIA,0,0],[0,MASS_2_INERTIA+(GEAR_RATIO**2)*MASS_3_INERTIA,0], [0,0,MASS_4_INERTIA]])
C = np.array([[0,0,0],[0,Ceq*(MASS_DIAMETER_2**2)/2+Ceq*(MASS_DIAMETER_3**2)/2*GEAR_RATIO**2,0],[0,0,0]])
K = np.array([[k1,-k1,0],[-k1,k1+(GEAR_RATIO**2)*k2,-GEAR_RATIO*k2],[0,-GEAR_RATIO*k2,k2]])
I = np.identity(dof)


# printing the calculated matrices above
print()
print("Mass Matrix:")
print()
print(M)
print()
print()
print("------------------")
print()
print("Damping Matrix:")
print()
print(C)
print()
print()
print("------------------")
print()
print("Stiffness Matrix:")
print()
print(K)
print()
print()

#--------------------------------------------------------

# Most of the values obtained for the eigenvectors + eigenvalues are
# not rounded off because rounding off too early causes calculation errors
# This was proven when other questions were used as a test
# Values are only rounded off for better presentation purposes only



evals, evecs = eigh(K,M)
evals=np.round(evals,4)
evals=abs(evals)
frequencies = np.sqrt(evals)


# printing the eigenvalues, eigen vectors and frequencies 
# from the calculations above
print("------------------")
print()
print("eigenvalues:")
print()
print(evals)
print()
print()
print("------------------")
print()
print("eigenvectors:")
print()
print(evecs)
print()
print()
print("------------------")
print()
print("frequencies in (rad/s):")
print()
print(frequencies)

#--------------------------------------------------------
