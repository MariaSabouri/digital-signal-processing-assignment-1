import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# -------------------------------------------------
# H(z) = 3/4 * z(z+1) / ((z+1/2)(z-1/4))
# Convert to standard polynomial form in z^-1
# -------------------------------------------------

# Poles and zeros directly from factored form:
zeros = np.array([0, -1])       # z=0 and z=-1
poles = np.array([-0.5, 0.25])  # z=-1/2 and z=1/4
gain = 3/4

# -------------------------------------------------
# Check stability: all poles must be inside |z|<1
# -------------------------------------------------
print("Poles:", poles)
print("Pole magnitudes:", np.abs(poles))
print("All poles inside unit circle?  -->", np.all(np.abs(poles) < 1))

# -------------------------------------------------
# Check causality: ROC is |z| > max|p_i|
# -------------------------------------------------
outermost_pole = np.max(np.abs(poles))
print("Outermost pole radius:", outermost_pole)
print("Causal ROC is: |z| >", outermost_pole)

# -------------------------------------------------
# Plot pole-zero diagram
# -------------------------------------------------
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
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
