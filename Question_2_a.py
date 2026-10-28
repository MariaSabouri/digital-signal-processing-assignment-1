import numpy as np
import matplotlib.pyplot as plt

def mat_coef(N):
    W_N = np.exp(-1j * 2 * np.pi / N)

    k = np.arange(N).reshape(N, 1)   
    n = np.arange(N).reshape(1, N)   

    matrix_coef = W_N ** (k * n)
    return matrix_coef

def plot_dft_idft(idft, dft):
    fig, axes = plt.subplots(nrows=1, ncols=2)

    axes[0].stem(np.abs(idft))
    axes[0].set_title("Original Signal")
    axes[0].grid(True)

    N = len(dft)
    omega = np.linspace(-np.pi, np.pi, N, endpoint=False)
    axes[1].stem(omega, np.abs(dft))
    axes[1].set_title("Magnitude Spectrum")
    axes[1].grid(True)

    plt.show()

#---------------------------------------------------------------------
dft = np.array([0.5, 0, 0, 0, 0.5, 0, 0, 0])
# print(np.shape(X))
inv_matrix_coef  = np.linalg.inv(mat_coef(8))

idft = inv_matrix_coef.dot(dft)
# dft = np.matmul(inv_matrix_coef, dft)
# dft = inv_matrix_coef @ dft
idft_rounded = np.round(idft.real, 3) + 1j*np.round(idft.imag, 3)
# print(idft_rounded)

# plot_dft_idft(idft = idft_rounded, dft = dft)
#----------------------------------------------------------------------

zero_padd = np.zeros((8,))
idft_2 = np.append(idft_rounded, zero_padd)
# print(idft_2)
matrix_coef = mat_coef(16)

dft_2 = matrix_coef.dot(idft_2)
dft_rounded_2 = np.round(dft_2.real, 3) + 1j*np.round(dft_2.imag, 3)
# print(dft_rounded_2)
# plot_dft_idft(idft = idft_2, dft = dft_rounded_2)

#----------------------------------------------------------------------

idft_3 = np.append(idft_rounded, idft_rounded)
# print(idft_3)
matrix_coef = mat_coef(16)
dft_3 = matrix_coef.dot(idft_3)
dft_rounded_3 = np.round(dft_3.real, 3) + 1j*np.round(dft_3.imag, 3)
# print(dft_rounded_3)
plot_dft_idft(idft = idft_3, dft = dft_rounded_3)

#----------------------------------------------------------------------

