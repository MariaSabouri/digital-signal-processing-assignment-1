import numpy as np
import matplotlib.pyplot as plt

def plot_fft(fs, N, f_signal, zero_padd = 0):
    t = np.arange(N) / fs
    x = np.sin(2 * np.pi * f_signal * t)
    t = np.arange(N + zero_padd) / fs
    x_fft = np.zeros(N + zero_padd)
    x_fft[0:N] = x[0:N]
    
    X = np.fft.fft(x, (N + zero_padd))
    X_mag = np.abs(X) / (N + zero_padd)
    f = np.fft.fftfreq(N + zero_padd, d=1/fs)
    
    # Plotting
    fig, axs = plt.subplots(2, 1, figsize=(8, 8))
    
    # Time-domain plot
    axs[0].stem(t, x_fft)
    axs[0].set_title(f'Time-domain Signal | fs={fs}Hz, N={N+zero_padd}')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Amplitude')
    axs[0].grid(True)
    
    # Frequency-domain (FFT) plot
    axs[1].stem(f[:N//2], X_mag[:N//2])
    axs[1].set_title(f'FFT Magnitude | fs={fs}Hz, N={N}')
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('|X(f)|')
    axs[1].grid(True)
    
    plt.tight_layout()
    plt.show()

# a
plot_fft(fs=64, N=128, zero_padd = 0, f_signal=12.5)

# b
plot_fft(fs=128, N=128, zero_padd = 0, f_signal=12.5)

# c
plot_fft(fs=128, N=128, zero_padd = 128 , f_signal=12.5)
