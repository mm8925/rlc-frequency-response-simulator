import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Component values
R = 100      # Resistance (ohms)
L = 0.1      # Inductance (H)
C = 1e-6     # Capacitance (F)

# Frequency range
f = np.logspace(1, 5, 300)  # 10 Hz to 100 kHz
w = 2 * np.pi * f

# Transfer function magnitude
H = 1 / np.sqrt((1 - w**2 * L * C)**2 + (w * R * C)**2)
H_db = 20 * np.log10(H)

# Resonant frequency
f0 = 1 / (2 * np.pi * np.sqrt(L * C))

print(f"Resonant Frequency: {f0:.2f} Hz")

# Plot setup
fig, ax = plt.subplots()
line, = ax.semilogx([], [], linewidth=2)

# Resonance marker
res_line = ax.axvline(f0, linestyle='--', label="Resonance Frequency")

ax.set_xlim(min(f), max(f))
ax.set_ylim(min(H_db), max(H_db))
ax.set_title("Animated RLC Frequency Response")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude (dB)")
ax.grid()
ax.legend()

# Animation function
def update(frame):
    line.set_data(f[:frame], H_db[:frame])
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=len(f), interval=30)

plt.show()