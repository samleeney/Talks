# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LaTeX Beamer presentation for EUCAIFCON 2025 about "Bayesian anomaly detection for Cosmology - 21cm, Supernovae, and beyond". The presentation covers theoretical and practical applications of anomaly detection methods in astronomical data analysis.

## Build Commands

### Compile the presentation
```bash
# Using latexmk (recommended - handles multiple passes automatically)
latexmk -pdf jax_bandflux_talk.tex

# Alternative: manual compilation with pdflatex
pdflatex jax_bandflux_talk.tex
pdflatex jax_bandflux_talk.tex  # Run twice for references

# Clean auxiliary files
latexmk -c jax_bandflux_talk.tex

# Clean all generated files including PDF
latexmk -C jax_bandflux_talk.tex
```

### Generate plots
```bash
# Individual plot generators (Python scripts)
python plot_generator.py
python bernoulli_prior_plot_generator.py
python gaussian_contour_plot_generator.py
python likelihood_floor_plot_generator.py
python log_likelihood_comparison_plot_generator.py
python marginalize_epsilon_plot_generator.py
python bernoulli_prior_weighted_likelihood_plot_generator.py
python dominant_mask_plot_generator.py
```

## Project Structure

- **Main presentation**: `jax_bandflux_talk.tex` - The LaTeX source for the Beamer presentation
- **Plot generators**: Python scripts that create figures for the presentation
  - Each script generates specific visualizations for different aspects of the anomaly detection methodology
- **images/**: Directory containing all figures and plots used in the presentation
  - `gif_anest/`: Contains frames for animated content (comb_1.png through comb_9.png)
- **Generated files**: `.aux`, `.log`, `.nav`, `.out`, `.pdf`, `.snm`, `.toc`, `.synctex.gz` - LaTeX compilation artifacts

## Key Technical Context

The presentation discusses:
1. Bayesian anomaly detection using an anomaly mask parameter ε
2. Applications to 21cm cosmology with the REACH telescope
3. JAX-bandflux tool for Type Ia supernova light curve fitting
4. Comparison between standard likelihood approaches and anomaly-aware likelihoods

When modifying the presentation, be aware that it uses:
- Beamer class with metropolis theme
- 16:9 aspect ratio
- animate package for animations
- tikz for diagrams
- natbib for bibliography management