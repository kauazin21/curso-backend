import numpy as np

a= np.array([1,2,3])
print(a)

print("arranjo criado com intervalo:")
z = np.arange(0,2,0.2,)
print(z)

print("criando uma matriz 3x3:")
w= np.ones((3,3))
print(w)

print("redimensionando:")
y = 5 * z
y.shape = 2,5
print(y)
print(y.flatten())

