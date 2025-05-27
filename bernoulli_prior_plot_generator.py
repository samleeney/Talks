import matplotlib.pyplot as plt
import numpy as np

def generate_bernoulli_prior_plot(p=0.1, output_filename="bernoulli_prior_plot.png"):
    """
    Generates a bar plot visualizing the Bernoulli Prior for anomaly detection.

    Args:
        p (float): The probability of an anomaly (epsilon_i = 1).
        output_filename (str): The name of the file to save the plot.
    """
    if not (0 <= p <= 1):
        raise ValueError("Probability p must be between 0 and 1.")

    # Probabilities
    prob_epsilon_0 = 1 - p
    prob_epsilon_1 = p

    # Labels for the bars
    labels = [r'$\epsilon_i = 0$ (Expected)', r'$\epsilon_i = 1$ (Anomalous)']
    probabilities = [prob_epsilon_0, prob_epsilon_1]

    # Create the bar plot
    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(labels, probabilities, color=['skyblue', 'salmon'])

    # Add labels and title
    ax.set_xlabel(r'Anomaly Status for a Single Data Point ($\epsilon_i$)', fontsize=12)
    ax.set_ylabel(r'Probability $P(\epsilon_i)$', fontsize=12)
    ax.set_title(f'Bernoulli Prior for Anomaly Detection (p={p})\n(Applied to a Dataset of 5 Points)', fontsize=14)
    ax.set_ylim(0, 1) # Probabilities are between 0 and 1

    # Add probability values on top of the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.02, round(yval, 2), ha='center', va='bottom', fontsize=10)
    
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)

    # Save the plot
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()

if __name__ == "__main__":
    # Choose a reasonable value for p
    anomaly_probability = 0.1

    # Generate and save the plot
    generate_bernoulli_prior_plot(p=anomaly_probability)
    print(f"Bernoulli Prior plot saved as bernoulli_prior_plot.png with p={anomaly_probability}")