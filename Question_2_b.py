import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
h = np.array([1, 1])
h_inv = h[::-1]
L = len(x)
P = len(h)
y_linear = np.zeros(P + L - 1)
y_circular = np.zeros(L)
#----------------------------linear convolution-------------------------------
for n in range(P + L - 1):
    aux_h = np.zeros((L + 2 * (P-1)))
    aux_h[n:(n + P)] = h_inv
    H = aux_h[P-1:(P-1) + L]
    y_linear[n] = np.sum(H * x)

print(y_linear)
#-------------------------circular convolution--------------------------------
for n in range(L):
    for k in range(P):
        y_circular[n] += h[k] * x[(n - k) % L]  
print(y_circular)  

    