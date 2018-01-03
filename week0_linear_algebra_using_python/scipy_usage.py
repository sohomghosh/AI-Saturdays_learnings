#Link: https://github.com/divyanshj16/ai-saturdays/blob/master/week0/SciPy.ipynb
import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,8]])

from scipy import linalg

#Determinant of a Matrix
# Compute the determinant of a matrix
linalg.det(A)

#Compute pivoted LU decomposition of a matrix. The decomposition is::   A = P L U    where P is a permutation matrix, L lower triangular with unit diagonal elements, and U upper triangular.
P, L, U = linalg.lu(A)

#We can find out the eigenvalues and eigenvectors of this matrix:
EW, EV = linalg.eig(A)

v = np.array([[2],[3],[5]])

s = linalg.solve(A,v)

#Function: spsolve
linalg.spsolve(A, b)

#Dot product : Matrix M and vector v
M.dot(v)

#Cross product : vector v1 and vector v2
np.cross(v1, v2, axisa = 0, axisb = 0).T

np.Multiply(M, v)

np.Multiply(v1, v2)

#Transpose
M.T

np.linalg.inv(M)

eigvals, eigvecs = np.linalg.eig(M)

#Singular Value Decomposition
U, S, Vtranspose = np.linalg.svd(M)
