#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Simulate time data
t = np.linspace(0, 2 * np.pi * 2, 500)  # two periods

# Simulate a clean sine wave
clean_sine_wave = np.sin(t)

# Simulate a noisy sine wave by adding Gaussian noise
noise = np.random.normal(0, 1, t.shape)
noisy_sine_wave = clean_sine_wave + noise

# Plot both waves with no background and save as SVG
plt.figure(figsize=(10, 6))
plt.plot(t, clean_sine_wave, label="Clean Sine Wave", color="blue", linewidth=10)
plt.axis("off")
plt.savefig("clean_sine_wave.svg", format="svg", transparent=True)
plt.close()

plt.figure(figsize=(10, 6))
plt.plot(
    t, noisy_sine_wave, label="Noisy Sine Wave", color="red", alpha=0.7, linewidth=10
)
plt.axis("off")
plt.savefig("noisy_sine_wave.svg", format="svg", transparent=True)
plt.close()
