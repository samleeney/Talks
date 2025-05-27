import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Define parameters for the 2D Gaussian (same as likelihood_floor_plot_generator.py)
mu = np.array([0, 0]) # Mean of the Gaussian
cov = np.array([[1, 0.5], [0.5, 1]]) # Covariance matrix

# Create a grid for x and c parameters (same as likelihood_floor_plot_generator.py)
x_vals = np.linspace(-3, 3, 100)
c_vals = np.linspace(-3, 3, 100)
X, C = np.meshgrid(x_vals, c_vals)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = C

# Calculate the PDF of the 2D Gaussian
Z_gaussian = multivariate_normal.pdf(pos, mean=mu, cov=cov)

# Create the 2D contour plot
plt.figure(figsize=(8, 7)) # Adjust figure size as needed

# Plot the contour
contour = plt.contourf(X, C, Z_gaussian, levels=50, cmap='viridis')
plt.colorbar(contour, label='Likelihood Value')

# Add labels and title
plt.xlabel('Parameter X', fontsize=12)
plt.ylabel('Parameter C', fontsize=12)
plt.title('2D Gaussian Likelihood Contour', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Save the plot
output_filename = 'images/gaussian_contour_plot.png'
plt.savefig(output_filename)
print(f"Plot saved as {output_filename}")

plt.close()