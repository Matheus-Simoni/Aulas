#matrizes
import  numpy as np

m = [[1, 3], [5, 6]]
n = [[8, 9], [3, 2]]

s=[[0,0], [0,0]]
for i in range(len(m)):
    for j in range(len(m)):
        s[i][j] = m[i][j]  + n[i][j]
print(s)

#biblioteca numpy
print(np.add(m,n))
print(np.transpose(m))
print(np.dot(m,n))

#resolvendo sistemas lineares
#x + 2y = 5
#3x -5y =4

A = np.array([[1, 2], [3, -5]])
B = np.array([5,4])
print(np.dot(np.linalg.inv(A), B))       