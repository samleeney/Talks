# Transition Slide: Connecting JAX-bandflux to Bayesian Anomaly Detection

## Purpose of This Document

This document provides a detailed explanation of the transition slide that connects the JAX-bandflux section to the Bayesian anomaly detection section. This transition is crucial for establishing the mathematical relationship between the SALT model parameters and the anomaly detection framework.

## The Transition Slide

```latex
\begin{frame}{Connecting SALT Models to Anomaly Detection}
  \begin{columns}
    \begin{column}{0.5\textwidth}
      \textbf{SALT Model Parameters:}
      \begin{itemize}
        \item $x_0$: Overall amplitude/normalization
        \item $x_1$: Stretch parameter (light curve width)
        \item $t_0$: Time of peak brightness
        \item $c$: Color parameter
      \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
      \textbf{Anomaly Detection Benefits:}
      \begin{itemize}
        \item More robust parameter estimation
        \item Automatic identification of outliers
        \item Improved distance measurements
        \item Reduced systematic errors
      \end{itemize}
    \end{column}
  \end{columns}
  
  \vspace{0.5cm}
  \begin{itemize}
    \item Traditional fitting minimizes $\chi^2$ without accounting for anomalies
    \item Our approach: Replace standard likelihood with anomaly-sensitive likelihood
    \item JAX enables efficient implementation through:
      \begin{itemize}
        \item Automatic differentiation for gradient-based optimization
        \item GPU acceleration for processing large datasets
        \item Vectorized operations for parallel processing
      \end{itemize}
  \end{itemize}
\end{frame}
```

## Detailed Explanation

### Key Mathematical Connection

The core mathematical connection between JAX-bandflux and Bayesian anomaly detection lies in how we handle the likelihood function for parameter estimation:

1. **Traditional SALT Fitting**:
   - Uses a standard chi-squared likelihood: $\mathcal{L}(\theta) = \exp(-\frac{1}{2}\sum_i \frac{(D_i - M_i(\theta))^2}{\sigma_i^2})$
   - Where $D_i$ are observed fluxes, $M_i(\theta)$ are model fluxes with parameters $\theta = \{x_0, x_1, t_0, c\}$
   - Assumes all data points are equally valid (no anomalies)

2. **Anomaly-Aware SALT Fitting**:
   - Uses a piecewise likelihood: $P(\mathcal{D}_i|\theta) = \begin{cases} \mathcal{L}_i(\theta) &: \text{expected}\\ \Delta^{-1}[ 0<\mathcal{D}_i<\Delta] &: \text{anomalous} \end{cases}$
   - Incorporates a Bernoulli prior: $P(\varepsilon_i) = p_i^{(1-\varepsilon_i)}(1-p_i)^{\varepsilon_i}$
   - Marginalizes over anomaly indicators: $P(\mathcal{D}|\theta) = \sum_{\varepsilon \in \{0,1\}^N} P(\mathcal{D},\varepsilon|\theta)$
   - Results in more robust parameter estimation

### Why This Connection Matters

1. **Parameter Estimation Robustness**:
   - $x_0$ (amplitude): Directly affects distance estimation; anomalies can bias distances
   - $x_1$ (stretch): Affects standardization; outliers can lead to incorrect classification
   - $t_0$ (peak time): Critical for phase determination; anomalies can shift apparent peak
   - $c$ (color): Affects extinction correction; anomalies can lead to incorrect reddening

2. **JAX Implementation Advantages**:
   - Automatic differentiation: Enables efficient gradient-based optimization of complex likelihood
   - GPU acceleration: Makes it feasible to process large datasets with the more complex likelihood
   - Vectorized operations: Allows parallel processing of multiple supernovae observations

### Visual Representation

Consider adding a diagram to this slide that shows:

```
┌───────────────────┐     ┌───────────────────┐     ┌───────────────────┐
│                   │     │                   │     │                   │
│   SALT Model      │     │  Anomaly-Aware    │     │  Improved         │
│   Parameters      │────▶│  Likelihood       │────▶│  Parameter        │
│   x₀, x₁, t₀, c   │     │  Function         │     │  Estimation       │
│                   │     │                   │     │                   │
└───────────────────┘     └───────────────────┘     └───────────────────┘
                                    ▲
                                    │
                          ┌───────────────────┐
                          │                   │
                          │  JAX              │
                          │  Implementation   │
                          │                   │
                          └───────────────────┘
```

## Placement in Presentation

This slide should be placed:
- After completing the explanation of JAX-bandflux and the SALT model (after slide 188)
- Before beginning the detailed explanation of Bayesian anomaly detection (before slide 340)

This positioning ensures that the audience understands the SALT model parameters before seeing how they connect to the anomaly detection framework.

## Key Points to Emphasize When Presenting

When presenting this slide, emphasize:

1. The **bidirectional benefit**:
   - JAX-bandflux provides efficient implementation of complex models
   - Anomaly detection improves the reliability of SALT parameter estimation

2. The **practical impact**:
   - More reliable distance measurements for cosmology
   - Reduced need for manual data cleaning
   - Ability to use more data that would otherwise be discarded

3. The **mathematical elegance**:
   - Principled Bayesian approach to handling outliers
   - Unified framework that works across different types of data

This transition slide serves as the conceptual bridge between the technical tools (JAX-bandflux) and the mathematical methodology (Bayesian anomaly detection), setting up the audience to understand how these components work together in the application to supernovae data.