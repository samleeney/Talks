import numpy as np
import matplotlib.pyplot as plt

# Define constants
p = 0.1
Delta = 10.0

# Calculate constant term: log(p) - log(Delta)
constant_term = np.log(p) - np.log(Delta)

# Define a range for log(L_i)
log_L_i = np.linspace(-10, 5, 500) # Adjust range as needed

# Calculate the first term: log(L_i) + log(1-p)
term1 = log_L_i + np.log(1 - p)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the first term
plt.plot(log_L_i, term1, label=r'$\log(L_i) + \log(1-p)$', color='blue')

# Plot the constant term
plt.axhline(y=constant_term, color='red', linestyle='--', label=r'$\log(p) - \log(\Delta)$')

# Find the intersection point
# The intersection occurs when log(L_i) + log(1-p) = log(p) - log(Delta)
# log(L_i) = log(p) - log(Delta) - log(1-p)
intersection_log_L_i = np.log(p) - np.log(Delta) - np.log(1 - p)

# Add a vertical line at the intersection point
plt.axvline(x=intersection_log_L_i, color='green', linestyle=':', label=f'Intersection at $\log(L_i) \\approx {intersection_log_L_i:.2f}$')

# Shade regions
# Region where epsilon_max = 1 (term1 > constant_term)
plt.fill_between(log_L_i, term1, constant_term, where=(term1 > constant_term), color='blue', alpha=0.1, interpolate=True, label=r'$\epsilon_{max} = 1$ region')
# Region where epsilon_max = 0 (term1 <= constant_term)
plt.fill_between(log_L_i, term1, constant_term, where=(term1 <= constant_term), color='red', alpha=0.1, interpolate=True, label=r'$\epsilon_{max} = 0$ region')


# Labels and Title
plt.xlabel(r'$\log(L_i)$', fontsize=14)
plt.ylabel('Log-Likelihood Term Value', fontsize=14)
plt.title(r'Log-Likelihood Term Comparison for $\epsilon_{max}$ Determination (per data point, for a dataset of 5)', fontsize=16)
plt.legend(fontsize=10)
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.ylim(min(constant_term, np.min(term1)) - 1, max(constant_term, np.max(term1)) + 1) # Adjust y-limits dynamically

# Save the plot
plt.savefig('log_likelihood_comparison_plot.png')
plt.close()

print("Plot 'log_likelihood_comparison_plot.png' generated successfully.")