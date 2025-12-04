import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# -----------------------------
# Define system H(z)
# -----------------------------
# Zeros at z = 0 and z = -1
zeros = np.array([0, -1])

# Poles at z = -1/2 and z = 1/4
poles = np.array([-0.5, 0.25])

# Gain from h[0] = 3/4
gain = 3/4

# Convert factored form (zeros, poles, gain) → polynomials b(z), a(z)
b = gain * np.poly(zeros)   # numerator
a = np.poly(poles)          # denominator

print("b(z) coefficients:", b)
print("a(z) coefficients:", a)

# -----------------------------
# Frequency response H(e^{jw})
# -----------------------------
w, h = sig.freqz(b, a, worN=2048)

plt.figure(figsize=(7,4))
plt.plot(w, np.abs(h))
plt.title("Frequency Response |H(e^{jw})|")
plt.xlabel("ω  (radians/sample)")
plt.ylabel("|H(e^{jw})|")
plt.grid(True)
plt.show()
