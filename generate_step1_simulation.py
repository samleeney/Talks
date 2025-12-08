"""
Generate a clean, high-contrast simulated dispersed pulse for the Step 1 slide.

This does not depend on the package simulator to keep the visual simple and bright.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def make_dispersion_delay(dm, freqs_mhz, k_delay=2.5e5):
    """Return integer sample delays for a given DM."""
    f_ref = freqs_mhz.max()
    delays = k_delay * dm * (1.0 / freqs_mhz**2 - 1.0 / f_ref**2)
    return np.round(delays).astype(int)


def main():
    n_freq = 96
    n_time = 480
    dm_true = 320.0
    pulse_time = 260
    pulse_width = 6.0
    pulse_amp = 8.0
    sigma_noise = 0.8

    freqs_mhz = np.linspace(900.0, 1600.0, n_freq)
    times_ms = np.arange(n_time, dtype=float)

    rng = np.random.default_rng(42)
    noise = rng.normal(0.0, sigma_noise, size=(n_freq, n_time))
    data = noise.copy()

    delays = make_dispersion_delay(dm_true, freqs_mhz)
    for i, delay in enumerate(delays):
        t_arrival = pulse_time + delay
        profile = pulse_amp * np.exp(-0.5 * ((times_ms - t_arrival) / pulse_width) ** 2)
        data[i] += profile

    # RFI-contaminated copy
    data_rfi = data.copy()
    # Very bright broadband hits
    data_rfi[:, 120:135] += 25.0
    data_rfi[:, 200:215] += 22.0
    data_rfi[:, 310:330] += 20.0
    data_rfi[:, 400:420] += 18.0
    # Multiple narrowband persistent lines
    data_rfi[6:14, :] += 15.0
    data_rfi[22:30, :] += 12.0
    data_rfi[48:54, :] += 10.0
    # Comb-like patches
    data_rfi[35:42, 150:240] += 16.0
    data_rfi[60:66, 260:340] += 14.0
    # Dense hot pixels
    rng = np.random.default_rng(123)
    for _ in range(80):
        fi = rng.integers(0, n_freq)
        ti = rng.integers(0, n_time)
        data_rfi[fi, ti] += rng.uniform(18.0, 28.0)

    out_dir = Path("images")
    out_dir.mkdir(parents=True, exist_ok=True)

    def save(fig_data, name):
        fig, ax = plt.subplots(figsize=(7.8, 4.4))
        im = ax.imshow(
            fig_data,
            origin="lower",
            aspect="auto",
            extent=[times_ms[0], times_ms[-1], freqs_mhz[0], freqs_mhz[-1]],
            cmap="magma",
        )
        ax.set_xlabel("Time (ms)")
        ax.set_ylabel("Frequency (MHz)")
        cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.02)
        cbar.set_label("Intensity (a.u.)")
        fig.tight_layout()
        out_path = out_dir / name
        fig.savefig(out_path, dpi=300, bbox_inches="tight")
        plt.close(fig)
        print(f"Saved {out_path}")

    save(data, "step1_simulated_pulse.png")
    save(data_rfi, "step1_simulated_pulse_rfi.png")


if __name__ == "__main__":
    main()
