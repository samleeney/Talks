"""
Generate a simulated dispersed pulse highlighting t0 as the asymptote (arrival at infinite frequency).
Outputs a PNG at images/t0_visual.png.
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
    n_time = 420
    dm_true = 350.0
    t0 = 150.0
    pulse_width = 6.0
    pulse_amp = 7.0
    sigma_noise = 1.2

    freqs_mhz = np.linspace(900.0, 1600.0, n_freq)
    times_ms = np.arange(n_time, dtype=float)

    rng = np.random.default_rng(7)
    data = rng.normal(0.0, sigma_noise, size=(n_freq, n_time))

    delays = make_dispersion_delay(dm_true, freqs_mhz)
    for i, delay in enumerate(delays):
        t_arrival = t0 + delay
        profile = pulse_amp * np.exp(-0.5 * ((times_ms - t_arrival) / pulse_width) ** 2)
        data[i] += profile

    out_path = Path("images/t0_visual.png")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(7.8, 4.2))
    im = ax.imshow(
        data,
        origin="lower",
        aspect="auto",
        extent=[times_ms[0], times_ms[-1], freqs_mhz[0], freqs_mhz[-1]],
        cmap="magma",
    )
    ax.axvline(t0, color="deepskyblue", ls="--", lw=2, label=r"$t_0'$ (asymptote)")
    ax.text(
        t0 + 3,
        freqs_mhz[-1] - 30,
        r"$t_0'$",
        color="deepskyblue",
        fontsize=11,
        va="top",
        ha="left",
    )
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Frequency (MHz)")
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.02)
    cbar.set_label("Intensity (a.u.)")
    ax.legend(loc="upper left", frameon=False)
    fig.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
