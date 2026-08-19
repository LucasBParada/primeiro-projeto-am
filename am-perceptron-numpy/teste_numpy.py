import numpy as np

x = np.array([8.0,7.0])
w = np.array([0.8,0.3])
bias = -7.0

z_dot = np.dot(x,w) + bias

z_operador = (x @ w) + bias

print("Z com np.dot: ", z_dot)
print("Z com operador @: ", z_operador)

