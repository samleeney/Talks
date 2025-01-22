import numpy as np
import matplotlib.pyplot as plt

# Parameters
np.random.seed(42)  # For reproducibility
N = 1000  # Number of data points
true_signal_amplitude = 10  # Amplitude of the sine wave
noise_level = 1  # Standard deviation of Gaussian noise
rfi_strength = 5  # Strength of RFI spikes, lower than the sine wave amplitude
rfi_indices = np.random.choice(N, size=10, replace=False)  # Random RFI positions

# Generate sine wave data
time = np.linspace(0, 4 * np.pi, N)
data = true_signal_amplitude * np.sin(time) + np.random.normal(0, noise_level, N)
data[rfi_indices] += rfi_strength  # Add RFI spikes

# Calculate mean and standard deviation
mu = np.mean(data)
sigma = np.std(data)

# Plot original data with multiple thresholds
plt.figure(figsize=(12, 6))
plt.plot(data, label='Original Data', color='blue')
plt.scatter(rfi_indices, data[rfi_indices], color='red', label='RFI', zorder=5)

# Plot thresholds for k values from 1 to 4
for k in range(1, 5):
    threshold = mu + k * sigma
    plt.axhline(y=threshold, linestyle='--', label=f'Threshold (k={k})')

plt.title('Sine Wave Data with RFI and Multiple Thresholds')
plt.xlabel('Time Index')
plt.ylabel('Signal Amplitude')
plt.legend()
plt.savefig('../images/threshold_sin_multiple.png', dpi=300, bbox_inches='tight')
plt.close()
