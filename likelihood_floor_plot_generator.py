import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# Define parameters for the 2D Gaussian
mu = np.array([0, 0]) # Mean of the Gaussian
cov = np.array([[1, 0.5], [0.5, 1]]) # Covariance matrix

# Create a grid for x and c parameters
x_vals = np.linspace(-3, 3, 100)
c_vals = np.linspace(-3, 3, 100)
X, C = np.meshgrid(x_vals, c_vals)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = C

# Calculate the PDF of the 2D Gaussian
Z_gaussian = multivariate_normal.pdf(pos, mean=mu, cov=cov)

# Define the "floor" value (representing the anomalous likelihood contribution)
# This value should be chosen to be "about 3/4 of the way down the likelihood"
# Let's pick a value relative to the peak of the Gaussian
max_gaussian_val = np.max(Z_gaussian)
floor_value = max_gaussian_val * 0.3 # Moving the floor down to 0.3

# Apply the floor: the likelihood cannot go below this value
Z_with_floor = np.maximum(Z_gaussian, floor_value)

# Create the 3D plot
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the 2D Gaussian with the floor (the visible part)
surf_visible = ax.plot_surface(X, C, Z_with_floor, cmap='viridis', edgecolor='none', alpha=0.8)

# Plot the flat plane (floor)
ax.plot_surface(X, C, np.full_like(X, floor_value), color='gray', alpha=0.5, rstride=100, cstride=100)

# Plot the part of the Gaussian that is below the floor (in a different color/transparency)
# Create a masked array for Z_gaussian where it's below the floor
Z_below_floor = np.where(Z_gaussian < floor_value, Z_gaussian, np.nan) # Use np.nan to hide parts above floor

surf_below = ax.plot_surface(X, C, Z_below_floor, cmap='Reds', edgecolor='none', alpha=0.3) # Use a different cmap and higher transparency

# Add labels and title
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('C', fontsize=12)
ax.set_zlabel('Likelihood', fontsize=12)
ax.set_title('2D Gaussian Likelihood with a Flat Floor at $p$', fontsize=16)

# Add a color bar
fig.colorbar(surf_visible, shrink=0.5, aspect=5, label='Likelihood Value')

# Adjust view angle for better visualization
ax.view_init(elev=30, azim=-120) # Adjust as needed

# Set z-axis limits to show below the floor
ax.set_zlim(0, max_gaussian_val * 1.1) # From 0 to slightly above the peak

# Save the plot
output_filename = 'images/likelihood_floor_plot.png'
plt.savefig(output_filename)
print(f"Plot saved as {output_filename}")

plt.close()