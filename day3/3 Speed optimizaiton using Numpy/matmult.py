# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 5

# NxN matrix
X = np.random.randint(0,100,(N,N))
print("X")
print(X)

# Nx(N+1) matrix
Y = np.random.randint(0,100,(N,N+1))
print("Y")
print(Y)

# X, Y dot product
result = np.dot(X,Y)
print("result")
print(result)