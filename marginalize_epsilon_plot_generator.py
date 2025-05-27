import matplotlib.pyplot as plt
import numpy as np
import itertools

def generate_marginalize_epsilon_plot():
    """
    Generates a plot visualizing the "Marginalize over epsilon" concept.
    This plot demonstrates summing over a representative subset of "masks"
    for 5 data points.
    """
    n_data_points = 5

    # Define a representative subset of masks for 5 data points
    masks = [
        (0, 0, 0, 0, 0),  # All expected
        (1, 1, 1, 1, 1),  # All anomalous
        (0, 0, 1, 0, 0),  # Single anomaly
        (0, 1, 0, 1, 0),  # Multiple anomalies
        (1, 0, 0, 0, 0),  # Single anomaly at start
        (0, 0, 0, 0, 1)   # Single anomaly at end
    ]

    # Determine grid size for subplots based on the selected masks
    n_masks = len(masks)
    n_cols = 3 # For better layout with 6 masks
    n_rows = int(np.ceil(n_masks / n_cols))

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 3, n_rows * 3), squeeze=False)
    axes = axes.flatten() # Flatten the 2D array of axes for easy iteration

    # Define colors for expected (0) and anomalous (1)
    colors = {0: 'blue', 1: 'red'}
    labels = {0: 'Expected (ε=0)', 1: 'Anomalous (ε=1)'}

    # Create a dummy x-axis for plotting points
    x_coords = np.arange(n_data_points)

    for i, mask in enumerate(masks):
        ax = axes[i]
        mask_str = ','.join(map(str, mask))
        ax.set_title(f'Mask: ({mask_str})', fontsize=14)
        ax.set_xticks(x_coords)
        ax.set_xticklabels([f'{j+1}' for j in range(n_data_points)], fontsize=10)
        ax.set_yticks([]) # No y-axis needed for this visualization
        ax.set_xlim(-0.5, n_data_points - 0.5) # Adjust x-limits to center points
        ax.set_xlabel('Data Point Index', fontsize=12)

        # Plot each data point according to its epsilon value in the current mask
        for j, epsilon in enumerate(mask):
            ax.plot(x_coords[j], 0, 'o', color=colors[epsilon], markersize=10,
                    label=labels[epsilon] if j == 0 else "") # Label only once per color

        # Add a legend to distinguish colors
        if i == 0: # Add legend to the first subplot or a dedicated one if preferred
            handles = [plt.Line2D([0], [0], marker='o', color='w', label=labels[0],
                                  markerfacecolor=colors[0], markersize=10),
                       plt.Line2D([0], [0], marker='o', color='w', label=labels[1],
                                  markerfacecolor=colors[1], markersize=10)]
            fig.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.0, 0.95), fontsize=12)


    # Hide any unused subplots
    for i in range(n_masks, len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to make space for suptitle
    plt.savefig('marginalize_epsilon_plot.png')
    plt.close(fig)

if __name__ == '__main__':
    generate_marginalize_epsilon_plot()
    print("Generated marginalize_epsilon_plot.png with representative masks for 5 data points.")