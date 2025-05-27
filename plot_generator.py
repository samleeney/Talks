import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define parameters for the distributions
mu_expected = 0.0  # Mean of the expected Gaussian distribution
sigma_expected = 1.0  # Standard deviation of the expected Gaussian distribution
delta_uniform = 4.0  # Width of the anomalous uniform distribution
min_uniform = -2.0  # Minimum value for the anomalous uniform distribution
max_uniform = min_uniform + delta_uniform # Maximum value for the anomalous uniform distribution

# Generate x values for plotting
x = np.linspace(-5, 5, 500)

# Calculate the expected likelihood (Gaussian PDF)
expected_likelihood = norm.pdf(x, mu_expected, sigma_expected)

# Calculate the anomalous likelihood (Uniform PDF)
anomalous_likelihood = np.zeros_like(x)
anomalous_likelihood[(x >= min_uniform) & (x <= max_uniform)] = 1.0 / delta_uniform

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the expected likelihood
plt.plot(x, expected_likelihood, label=r'Expected Likelihood $L_i(\theta)$ (Gaussian)', color='blue')

# Plot the anomalous likelihood
plt.plot(x, anomalous_likelihood, label=r'Anomalous Likelihood $\Delta^{-1}[0 < D_i < \Delta]$ (Uniform)', color='red', linestyle='--')

# Define 5 example data points
data_points_values = np.array([-3.0, -1.0, 0.0, 2.0, 4.0])

# Calculate expected likelihood for these points
expected_likelihood_at_points = norm.pdf(data_points_values, mu_expected, sigma_expected)

# Calculate anomalous likelihood for these points
anomalous_likelihood_at_points = np.zeros_like(data_points_values, dtype=float)
for i, dp_val in enumerate(data_points_values):
    if min_uniform <= dp_val <= max_uniform:
        anomalous_likelihood_at_points[i] = 1.0 / delta_uniform

# Plot the example data points
plt.scatter(data_points_values, expected_likelihood_at_points,
            color='green', s=100, zorder=5, label='Example Data Points (Expected)')

# Plot anomalous likelihood for points within the uniform range
mask_uniform = (data_points_values >= min_uniform) & (data_points_values <= max_uniform)
plt.scatter(data_points_values[mask_uniform], anomalous_likelihood_at_points[mask_uniform],
            color='red', marker='x', s=100, zorder=5, label='Example Data Points (Anomalous)')

# Add labels and title with specified font sizes
plt.xlabel('Data Value ($D_i$)', fontsize=14)
plt.ylabel('Likelihood', fontsize=14)
plt.title('Piecewise Likelihood Concept', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.ylim(bottom=0) # Ensure y-axis starts at 0
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Save the plot
output_filename = 'piecewise_likelihood_plot.png'
plt.savefig(output_filename)
print(f"Plot saved as {output_filename}")

plt.close()