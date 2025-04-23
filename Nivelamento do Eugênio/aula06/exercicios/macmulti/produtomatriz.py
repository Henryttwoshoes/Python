import numpy as np

matriz34 = np.array([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12]])

matriz42 = np.array([[1,2],
                     [3,4],
                     [5,6],
                     [7,8]])


m = 3
n = 4
p = 2

produto = np.zeros((m,p))

for i in range(m):
    for j in range(p):
        for k in range(n):
            produto[i,j] += matriz34[i,k]*matriz42[k,j]
print(produto)