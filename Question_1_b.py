import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


zeros = np.array([0, -1])
poles = np.array([-0.5, 0.25])
gain = 3/4
b = gain * np.poly(zeros)  
a = np.poly(poles)     
# print(b)
# print(a)

# Frequency response
w, h = sig.freqz(b, a, worN=2048)

plt.figure(figsize=(7,4))
plt.plot(w, np.abs(h))
plt.title("Frequency Response |H(e^{jw})|")
plt.xlabel("ω  (radians/sample)")
plt.ylabel("|H(e^{jw})|")
plt.grid(True)
plt.show()
