import scipy.linalg as linalg
import numpy as np

A = np.array([[1, -2, 3], [4, 5, 5], [7, 1, 9]])
b = np.array([1, 2, 3])
print("a")
print(A)
print("b")
print(b)

# Solving the linear system of equation Ax = b
x = linalg.solve(A, b)
print("c")
print(x)

# Checking of the correctness by plugging the result back into the eqn
d = A.dot(x)
print("d")
print(d)

#Solving the linear system of equation Ax = B
B = np.random.rand(3,3)
print("B")
print(B)
x2 = linalg.solve(A, B)
print("x2")
print(x2)

# Checking of the correctness by plugging the result back into the eqn
e = A.dot(x2)
print("e")
print(e)

# Eigenvalues problem solving for the matrix A
f_eigenvalues, f_eigenvectors = linalg.eig(A)
print("f")
print(" eigenvalues")
print(f_eigenvalues)
print(" eigenvectors")
print(f_eigenvectors)

# Inverse , determinat of A
g_inverse = np.linalg.inv(A)
print("g_inverse")
print(g_inverse)

g_determinant = np.linalg.det(A)
print("g_determinant")
print(g_determinant)

# Norm of A with different orders
frobenius_norm = linalg.norm(A, 'fro')  # Frobenius norm
nuclear_norm = linalg.norm(A, 'nuc')    # Nuclear norm
linf_norm = linalg.norm(A, np.inf)  # Linf norm
l1_norm = linalg.norm(A, 1)  # L1 norm
l2_norm = linalg.norm(A, 2)  # L2 norm

print("h")
print("Frobenius Norm:", frobenius_norm)
print("Nuclear Norm:", nuclear_norm)
print("Linf Norm:", linf_norm)
print("L1 Norm:", l1_norm)
print("L2 Norm:", l2_norm)
