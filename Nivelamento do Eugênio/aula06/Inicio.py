import numpy as np

v1 = np.array([1,2,3,4,5])
v2 = np.arange(0,10,2)
v3 = np.linspace(0,10,6)
v4 = np.linspace(0,1,6)
v5 = np.linspace(0,1,7)
v6 = np.linspace(0,1,8)
v7 = np.linspace(0,1,9)

print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)
print(v7)
v0 = np.zeros(10)
print(v0)
vones = np.ones(7)
print(vones)

vsoma = v1 + 2
print(vsoma)
vmult = v1 * 7
print(vmult)
vq = v1 ** 2
print(vq)

rq = np.sqrt(vq)

print(rq)