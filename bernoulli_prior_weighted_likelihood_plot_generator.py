import numpy as np
import matplotlib.pyplot as plt

# Define the Bernoulli prior parameter
p = 0.1 # Probability of a data point being anomalous (epsilon=1)

# Define hypothetical likelihood values for each data point from dominant_mask_plot_generator.py
likelihood_expected = np.array([0.01, 0.9, 0.9, 0.9, 0.9])
likelihood_anomalous = np.array([10.0, 0.001, 0.001, 0.001, 0.001])

# Apply Bernoulli prior weights
weighted_expected_likelihood = likelihood_expected * (1 - p)
weighted_anomalous_likelihood = likelihood_anomalous * p

# Create x-coordinates for the discrete data points
x_coords = np.arange(len(likelihood_expected))

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the weighted expected likelihood for each data point
plt.scatter(x_coords, weighted_expected_likelihood, label=r'Weighted Expected Likelihood $L_i(\theta)(1-p)$', color='blue', zorder=5)

# Plot the weighted anomalous likelihood for each data point
plt.scatter(x_coords, weighted_anomalous_likelihood, label=r'Weighted Anomalous Likelihood $p/\Delta$', color='red', marker='x', s=100, zorder=5)

# Add labels and title
plt.xlabel('Data Point Index', fontsize=14)
plt.ylabel('Weighted Likelihood', fontsize=14)
plt.title('Bernoulli Prior Weighted Likelihoods (Discrete Data)', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.ylim(bottom=0) # Ensure y-axis starts at 0
plt.xticks(x_coords, [f'DP {i+1}' for i in x_coords], fontsize=12)
plt.yticks(fontsize=12)

# Save the plot
output_filename = 'images/bernoulli_prior_weighted_likelihood_plot.png'
plt.savefig(output_filename)
print(f"Plot saved as {output_filename}")

plt.close()