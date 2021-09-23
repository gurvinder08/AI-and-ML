import numpy as np
#Addition
A=np.array([[1,2,5],[4,5,0]], dtype=int)
B=np.array([[3,2,1],[1,4,7]], dtype=int)
print('First Matrix:\n',A)
print('Second Matrix:\n',B)
C=np.zeros((2,3), dtype=int)

for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j] + B[i][j]

print("Addition of 2 matrices:\n",C)

#Transpose of matrix A
print()
print('Matrix A:\n',A)
T = np.zeros((3,2), dtype=int)

for a in range(len(A)):
    for b in range(len(A[0])):
        T[b][a] = A[a][b]

print("Transpose of A:\n",T)
print(len(A[0]))
