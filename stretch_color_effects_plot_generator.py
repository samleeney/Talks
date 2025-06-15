import numpy as np
import matplotlib.pyplot as plt

def supernova_flux(t, t_max=0, x0=1.0, x1=0.0, c=0.0):
    """
    Generate a supernova light curve flux.
    
    Parameters:
    - t: time array (days from peak)
    - t_max: time of maximum light
    - x0: amplitude parameter
    - x1: stretch parameter (-3 to 3, positive = broader/slower)
    - c: color parameter (-0.3 to 0.3, positive = redder = dimmer)
    """
    # Time stretch factor
    stretch_factor = 1 + 0.1 * x1
    t_stretched = (t - t_max) / stretch_factor
    
    # Base template - asymmetric Gaussian-like shape
    rise_sigma = 15
    fall_sigma = 35
    
    flux = np.zeros_like(t)
    rise_mask = t_stretched <= 0
    fall_mask = t_stretched > 0
    
    # Rising part
    flux[rise_mask] = np.exp(-0.5 * (t_stretched[rise_mask] / rise_sigma)**2)
    # Falling part
    flux[fall_mask] = np.exp(-0.5 * (t_stretched[fall_mask] / fall_sigma)**2)
    
    # Apply amplitude
    flux *= x0
    
    # Apply color correction
    color_correction = 10**(-0.4 * c * 0.1 * (t_stretched + 20))
    flux *= color_correction
    
    return flux

def flux_to_magnitude(flux, zeropoint=25.0):
    """Convert flux to magnitude."""
    flux_safe = np.maximum(flux, 1e-10)
    return -2.5 * np.log10(flux_safe) + zeropoint

# Time array (days from peak) - focused on the main decline
t = np.linspace(-20, 60, 200)

# Generate the three example light curves showing effects
flux_base = supernova_flux(t, x0=1.0, x1=0, c=0)
flux_stretched = supernova_flux(t, x0=1.0, x1=1.5, c=0)
flux_colored = supernova_flux(t, x0=1.0, x1=0, c=0.15)

# Convert to magnitudes
mag_base = flux_to_magnitude(flux_base)
mag_stretched = flux_to_magnitude(flux_stretched)
mag_colored = flux_to_magnitude(flux_colored)

# Create single panel plot (slightly smaller)
fig, ax = plt.subplots(figsize=(7, 5))

ax.plot(t, mag_base, 'k-', linewidth=3, label='Standard (x₁=0, c=0)')
ax.plot(t, mag_stretched, 'b--', linewidth=3, label='Stretched (x₁=1.5)')
ax.plot(t, mag_colored, 'r:', linewidth=3, label='Reddened (c=0.15)')

ax.set_xlabel('Days from Peak', fontsize=14)
ax.set_ylabel('Magnitude', fontsize=14)
ax.set_title('Effects of Stretch and Color Parameters', fontsize=16, fontweight='bold')
ax.invert_yaxis()
ax.legend(fontsize=12, loc='upper right')
ax.grid(True, alpha=0.3)
ax.set_xlim(-20, 60)

# Add explanatory text (moved to bottom)
ax.text(0.02, 0.25, 'Stretch (x₁): Controls light curve width\nColor (c): Controls overall brightness', 
        transform=ax.transAxes, fontsize=11, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

# Save the plot
output_filename = 'images/stretch_color_effects_plot.png'
plt.tight_layout()
plt.savefig(output_filename, dpi=150, bbox_inches='tight')
print(f"Plot saved as {output_filename}")

plt.close()