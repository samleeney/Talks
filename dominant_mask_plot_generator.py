import numpy as np
import matplotlib.pyplot as plt

# 1. Define parameters
N_points = 5  # Number of data points

# 2. Define hypothetical likelihood values for each data point
# For point 0, it's truly anomalous: high likelihood_anomalous, low likelihood_expected
# For points 1,2,3, they are truly expected: high likelihood_expected, low likelihood_anomalous
likelihood_expected = np.array([0.01, 0.9, 0.9, 0.9, 0.9])
likelihood_anomalous = np.array([10.0, 0.001, 0.001, 0.001, 0.001])

# 3. Define the "epsilon_max" mask (the approximate correct mask)
# Here, point 0 is anomalous (1), others are expected (0)
epsilon_max_mask = np.array([1, 0, 0, 0, 0])

# 4. Generate a set of different masks
masks = []
mask_labels = []
dominant_mask_index = -1

# Add epsilon_max_mask first
masks.append(epsilon_max_mask)
mask_labels.append("Epsilon_max (Correct)")
dominant_mask_index = 0

# Generate other random masks, ensuring they are distinct and not too many
num_other_masks = 5
generated_masks_set = {tuple(epsilon_max_mask)} # Use tuple for set membership check

while len(masks) < num_other_masks + 1:
    new_mask = np.random.randint(0, 2, N_points)
    if tuple(new_mask) not in generated_masks_set:
        masks.append(new_mask)
        mask_labels.append(f"Mask {len(masks) - 1}")
        generated_masks_set.add(tuple(new_mask))

# 5. Calculate the total likelihood for each mask
total_likelihoods = []
for mask in masks:
    likelihood_for_mask = np.where(mask == 0, likelihood_expected, likelihood_anomalous)
    total_likelihood = np.prod(likelihood_for_mask)
    total_likelihoods.append(total_likelihood)

# Convert to numpy arrays for easier plotting
total_likelihoods = np.array(total_likelihoods)

# 6. Create the plot
plt.figure(figsize=(10, 6))
bars = plt.bar(mask_labels, total_likelihoods, color='skyblue')

# Highlight the epsilon_max mask
bars[dominant_mask_index].set_color('red')
bars[dominant_mask_index].set_label('Epsilon_max (Correct Mask)')

# Add labels and title
plt.xlabel("Mask Configuration", fontsize=14)
plt.ylabel("Total Likelihood", fontsize=14)
plt.title("Total Likelihood for Different Mask Configurations\n('Approximate correct mask is most likely')", fontsize=16)
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.yticks(fontsize=10)
plt.yscale('log') # Use log scale to better show the dominance if values vary widely
plt.legend(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# 7. Save the plot
output_filename = "dominant_mask_plot.png"
plt.savefig(output_filename)
plt.close()

print(f"Plot saved to {output_filename}")