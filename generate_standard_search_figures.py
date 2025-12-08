"""
Generate illustrative figures for the “How do standard search algorithms work?” section.

Creates a small set of PNGs under images/ showing:
1) Raw dynamic spectrum with RFI and collapsed S/N (no dedispersion).
2) The same data after simple RFI flagging.
3) Dedispersion trials at sub-optimal and optimal DMs, showing S/N growth.

Only depends on numpy and matplotlib.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def make_dispersion_delay(dm, freqs_mhz, k_delay=2.5e5):
    """Return integer sample delays for a given DM."""
    f_ref = freqs_mhz.max()
    delays = k_delay * dm * (1.0 / freqs_mhz**2 - 1.0 / f_ref**2)
    return np.round(delays).astype(int)


def simulate_dynamic_spectrum(
    n_freq=64,
    n_time=512,
    dm_true=520.0,
    pulse_time=270,
    pulse_width=5.0,
    pulse_amp=1.8,
    seed=7,
):
    """Simulate a dispersed pulse with broadband and narrowband RFI injected."""
    rng = np.random.default_rng(seed)
    freqs_mhz = np.linspace(900.0, 1600.0, n_freq)
    times_ms = np.arange(n_time, dtype=float)

    noise = rng.normal(0.0, 1.0, size=(n_freq, n_time))
    data = noise.copy()

    # Add dispersed astrophysical pulse.
    delays = make_dispersion_delay(dm_true, freqs_mhz)
    for i, delay in enumerate(delays):
        t_arrival = pulse_time + delay
        profile = pulse_amp * np.exp(-0.5 * ((times_ms - t_arrival) / pulse_width) ** 2)
        data[i] += profile

    # Add multiple RFI patterns.
    data[:, 165:175] += 12.0  # broadband blip across all freqs
    data[:, 330:340] += 10.0  # second broadband hit
    data[6:12, :] += 7.5 * (0.3 + rng.random(size=(6, n_time)))  # persistent narrowband
    data[30:34, 80:180] += 11.0  # localised comb
    for _ in range(12):  # scattered hot pixels
        fi = rng.integers(0, n_freq)
        ti = rng.integers(0, n_time)
        data[fi, ti] += rng.uniform(12.0, 16.0)

    # Mask describing what we would flag.
    mask = np.zeros_like(data, dtype=bool)
    mask[:, 165:175] = True  # broadband glitch
    mask[:, 330:340] = True  # second broadband
    mask[6:12, :] = True  # narrowband slice
    mask[30:34, 80:180] = True  # localised comb
    for _ in range(12):
        fi = rng.integers(0, n_freq)
        ti = rng.integers(0, n_time)
        mask[fi, ti] = True

    # Cleaned version replaces flagged samples with fresh noise matching background stats.
    cleaned = data.copy()
    base_mean = float(noise[~mask].mean())
    base_std = float(noise[~mask].std())
    cleaned[mask] = rng.normal(base_mean, base_std, size=cleaned[mask].shape)
    return freqs_mhz, times_ms, data, cleaned, mask


def dedisperse_snr(data, freqs_mhz, dm_trial, mask=None):
    """Dedisperse by integer shifts and return normalised S/N time series."""
    delays = make_dispersion_delay(dm_trial, freqs_mhz)

    stacked = []
    for chan, delay in zip(data, delays):
        shifted = np.roll(chan, -delay)
        stacked.append(shifted)
    stacked = np.stack(stacked)

    if mask is not None:
        stacked = np.ma.array(stacked, mask=np.broadcast_to(mask, stacked.shape))
        ts = stacked.mean(axis=0)
    else:
        ts = stacked.mean(axis=0)

    ts = ts - ts.mean()
    snr = ts / ts.std()
    return np.asarray(np.ma.filled(snr, fill_value=np.nan)).flatten()


def dedisperse_cube(data, freqs_mhz, dm_trial, mask=None):
    """Return a dedispersed dynamic spectrum for visualisation."""
    delays = make_dispersion_delay(dm_trial, freqs_mhz)
    shifted = []
    for chan, delay in zip(data, delays):
        shifted.append(np.roll(chan, -delay))
    cube = np.stack(shifted)
    if mask is not None:
        # Fill masked regions with noise-level values so plots show no holes.
        cube = np.ma.array(cube, mask=np.broadcast_to(mask, cube.shape))
        filled = np.ma.filled(cube, fill_value=np.median(cube))
        return filled
    return cube


def plot_state(
    freqs_mhz,
    times_ms,
    data,
    mask,
    snr,
    dm_label,
    title,
    outfile,
    threshold=6.0,
    show_mask_as_gray=False,
):
    """Plot dynamic spectrum (top) and dedispersed S/N (bottom)."""
    outfile.parent.mkdir(parents=True, exist_ok=True)

    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, figsize=(8.2, 6.2), gridspec_kw={"height_ratios": [2.1, 1.0]}
    )

    cmap = plt.get_cmap("magma")
    if show_mask_as_gray:
        cmap.set_bad(color="lightgray")
    data_to_show = np.ma.array(data, mask=mask if mask is not None else False)

    im = ax_top.imshow(
        data_to_show,
        origin="lower",
        aspect="auto",
        cmap=cmap,
        extent=[times_ms[0], times_ms[-1], freqs_mhz[0], freqs_mhz[-1]],
    )
    ax_top.set_ylabel("Frequency (MHz)")
    ax_top.set_title(title, fontsize=11)
    cbar = fig.colorbar(im, ax=ax_top, fraction=0.046, pad=0.02)
    cbar.set_label("Intensity (a.u.)")

    ax_bot.plot(times_ms, snr, color="#004b8d", lw=2)
    ax_bot.axhline(threshold, color="tomato", ls="--", lw=1.5, label="S/N threshold")
    ax_bot.set_xlabel("Time (ms)")
    ax_bot.set_ylabel("S/N (dedispersed)")
    ax_bot.set_xlim(times_ms[0], times_ms[-1])
    ax_bot.grid(alpha=0.3)
    ax_bot.legend(loc="upper right", frameon=False)
    ax_bot.text(
        0.01,
        0.9,
        f"Trial DM = {dm_label}",
        transform=ax_bot.transAxes,
        fontsize=10,
        ha="left",
        va="top",
    )

    # Mark peak if above threshold.
    peak_idx = int(np.argmax(snr))
    peak_val = snr[peak_idx]
    if peak_val > threshold:
        ax_bot.plot(times_ms[peak_idx], peak_val, marker="o", color="black")

    fig.tight_layout()
    fig.savefig(outfile, dpi=250, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {outfile}")


def main():
    freqs_mhz, times_ms, raw, cleaned, mask = simulate_dynamic_spectrum()

    outputs = []

    # Raw, no dedispersion.
    snr_raw = dedisperse_snr(raw, freqs_mhz, dm_trial=0.0)
    outputs.append(
        (raw, None, snr_raw, "0 (no dedispersion)", "Raw dynamic spectrum with RFI", "standard_search_raw.png")
    )

    # After manual flagging.
    snr_flagged = dedisperse_snr(cleaned, freqs_mhz, dm_trial=0.0, mask=mask)
    outputs.append(
        (
            cleaned,
            None,  # visual: show noise-filled data without gray holes
            snr_flagged,
            "0 (after flagging only)",
            "Flagged RFI before dedispersion",
            "standard_search_flagged.png",
        )
    )

    # Dedispersion sweeps.
    dm_trials = [50.0, 100.0, 150.0, 200.0, 250.0, 300.0, 380.0, 440.0, 520.0, 700.0]
    titles = [
        "DM 50: heavy under-correction (still swept)",
        "DM 100: under-corrected, faint rise",
        "DM 150: under-corrected but improving",
        "DM 200: partial straightening",
        "DM 250: closer, still smeared",
        "DM 300: closer alignment, still smeared",
        "DM 380: nearly straight, marginal S/N",
        "DM 440: close to peak alignment",
        "DM 520: straightened pulse, peak S/N",
        "DM 700: over-corrected and re-smeared",
    ]
    names = [
        "standard_search_dm050.png",
        "standard_search_dm100.png",
        "standard_search_dm150.png",
        "standard_search_dm200.png",
        "standard_search_dm250.png",
        "standard_search_dm300.png",
        "standard_search_dm380.png",
        "standard_search_dm440.png",
        "standard_search_dm520.png",
        "standard_search_dm700.png",
    ]

    for dm, title, name in zip(dm_trials, titles, names):
        snr_trial = dedisperse_snr(cleaned, freqs_mhz, dm_trial=dm, mask=mask)
        dedisp_cube = dedisperse_cube(cleaned, freqs_mhz, dm_trial=dm)  # show filled data, no holes
        outputs.append((dedisp_cube, None, snr_trial, f"{dm:.0f}", title, name))

    for data, mask_use, snr, dm_label, title, filename in outputs:
        plot_state(
            freqs_mhz=freqs_mhz,
            times_ms=times_ms,
            data=data,
            mask=mask_use,
            snr=snr,
            dm_label=dm_label,
            title=title,
            outfile=Path("images") / filename,
            show_mask_as_gray=mask_use is not None,
        )


if __name__ == "__main__":
    main()
