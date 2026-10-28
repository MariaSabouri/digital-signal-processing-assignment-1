import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


# Poles and zeros 
zeros = np.array([0, -1])       
poles = np.array([-0.5, 0.25])  
gain = 3/4


# Check
# print(poles)
# print(np.abs(poles))
print("All poles inside unit circle?", np.all(np.abs(poles) < 1))


# causality
outermost_pole = np.max(np.abs(poles))
# print(outermost_pole)


# Plot(this part of code is done by chat gpt)
plt.figure(figsize=(5,5))

# Plot unit circle
theta = np.linspace(0, 2*np.pi, 400)
plt.plot(np.cos(theta), np.sin(theta), 'k--', label='unit circle')

# Plot zeros and poles
plt.scatter(np.real(zeros), np.sin(0*zeros), marker='o', facecolors='none', edgecolors='b', s=120, label='zeros')
plt.scatter(np.real(poles), np.sin(0*poles), marker='x', color='r', s=120, label='poles')

# Since all zeros/poles are real, imaginary part is 0
# For completeness, plot them on real axis:
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', facecolors='none', edgecolors='b', s=120)
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', s=120)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title("Pole–Zero Plot of the System")
plt.xlabel("Real axis")
plt.ylabel("Imag axis")
# plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
