import numpy as np
import matplotlib.pyplot as plt

# Parameters
np.random.seed(42)  # For reproducibility
N = 1000  # Number of data points
true_signal = 10  # Flat line value
noise_level = 1  # Standard deviation of Gaussian noise
rfi_strength = 20  # Strength of RFI spikes
rfi_indices = np.random.choice(N, size=10, replace=False)  # Random RFI positions

# Generate data
data = true_signal + np.random.normal(0, noise_level, N)
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

plt.title('Original Data with RFI and Multiple Thresholds')
plt.xlabel('Time Index')
plt.ylabel('Signal Amplitude')
plt.legend()
plt.savefig('../images/threshold_multiple.png', dpi=300, bbox_inches='tight')
plt.close()

k = 3
threshold = mu + k * sigma
rfi_mask = data > threshold
cleaned_data = np.copy(data)
cleaned_data[rfi_mask] = np.nan  # Replace RFI with NaN

# Plot cleaned data
plt.figure(figsize=(12, 6))
plt.plot(cleaned_data, label='Cleaned Data', color='blue')
plt.axhline(y=threshold, color='green', linestyle='--', label=f'Threshold (k={k})')
plt.title('Data after RFI Removal')
plt.xlabel('Time Index')
plt.ylabel('Signal Amplitude')
plt.legend()
plt.savefig('../images/threshold_cleaned.png', dpi=300, bbox_inches='tight')
plt.close()