# Enhanced "Anomalous Measurements in SALT Fitting" Slide

## Purpose of This Document

This document provides a detailed explanation of how to enhance the "Anomalous measurements in SALT fitting" slide (slide 617) to better connect the SALT model parameters to the anomaly detection framework and demonstrate the practical benefits of the approach.

## The Enhanced Slide

```latex
\begin{frame}{Anomalous measurements in SALT fitting}
  \begin{itemize}
    \item Applying our Bayesian anomaly detection method to SALT fitting:
      \begin{itemize}
        \item Replace standard $\chi^2$ likelihood with anomaly-sensitive likelihood
        \item Automatically identifies outlier measurements
        \item Downweights anomalous data points during fitting
        \item Preserves information from non-anomalous measurements
      \end{itemize}
    \item Impact on SALT parameters:
      \begin{itemize}
        \item More accurate $x_0$ → Better distance estimates
        \item More reliable $x_1$ → Improved standardization
        \item More precise $t_0$ → Better phase determination
        \item More robust $c$ → Reduced extinction systematics
      \end{itemize}
    \item Implementation in JAX-bandflux:
      \begin{itemize}
        \item Fully differentiable pipeline enables gradient-based optimization
        \item GPU acceleration allows rapid processing of large datasets
        \item Automatic flagging of problematic data points
      \end{itemize}
  \end{itemize}
  
  \vspace{0.5cm}
  \centering
  [IMAGE: Data with anomalies]
\end{frame}
```

## Detailed Explanation

### Key Enhancements to the Original Slide

The original slide (617) focuses primarily on the general benefits of applying anomaly detection to SALT fitting but lacks specific connections to the SALT parameters. The enhanced version adds:

1. **Direct Parameter Impact Section**
   - Explicitly shows how each SALT parameter benefits from anomaly detection
   - Creates a clear connection between the mathematical framework and practical outcomes
   - Helps the audience understand the specific improvements, not just general benefits

2. **Implementation Details**
   - Highlights how JAX-bandflux enables the practical implementation
   - Connects back to the JAX capabilities discussed in the first section
   - Emphasizes the computational advantages that make this approach feasible

### Parameter-Specific Benefits Explanation

#### $x_0$ (Amplitude/Normalization)

- **Original issue**: Anomalous flux measurements directly bias the overall amplitude parameter
- **Consequence**: Incorrect distance estimates, affecting cosmological measurements
- **Improvement**: Anomaly detection identifies and downweights outlier flux measurements
- **Result**: More accurate $x_0$ values lead to more reliable distance estimates

#### $x_1$ (Stretch Parameter)

- **Original issue**: Outliers can distort the apparent light curve width
- **Consequence**: Incorrect standardization of supernovae luminosities
- **Improvement**: Anomaly detection preserves the true light curve shape
- **Result**: More reliable $x_1$ values improve the standardization process

#### $t_0$ (Time of Peak Brightness)

- **Original issue**: Anomalous measurements near peak can shift the apparent maximum
- **Consequence**: Incorrect phase determination affects all other parameter estimates
- **Improvement**: Robust determination of peak time even with outliers
- **Result**: More precise $t_0$ values provide better reference for all phase-dependent analyses

#### $c$ (Color Parameter)

- **Original issue**: Outliers in specific bandpasses can bias color estimates
- **Consequence**: Incorrect extinction corrections
- **Improvement**: Anomaly detection identifies bandpass-specific issues
- **Result**: More robust $c$ values lead to better handling of dust extinction

### Visual Component Recommendation

The placeholder "[IMAGE: Data with anomalies]" should be replaced with a figure showing:

1. A multi-band light curve with some anomalous data points
2. Visual indication of which points are identified as anomalous
3. Comparison of fitted curves with and without anomaly detection
4. Resulting parameter values showing the differences

An ideal image would have:
- Multiple bandpasses shown in different colors
- Anomalous points highlighted with a different symbol
- Two fitted curves (traditional and anomaly-aware)
- A small table showing parameter values and uncertainties for both methods

### Placement in Presentation

This enhanced slide should remain in its current position (slide 617) in the "Results on 1a supernovae" section, but ensure that:

1. It follows logically from the previous slides on SALT models
2. It precedes the slides on specific results and improvements
3. It connects clearly to the transition slide added between sections

### Presentation Tips

When presenting this slide:

1. **Emphasize the Direct Connection**
   - Explicitly point out how each SALT parameter benefits from anomaly detection
   - Use concrete examples if possible (e.g., "When a cosmic ray hits the detector...")

2. **Highlight the Practical Implementation**
   - Remind the audience how JAX makes this approach computationally feasible
   - Emphasize that without GPU acceleration, this method would be too slow for large datasets

3. **Connect to the Broader Impact**
   - Explain how these parameter improvements translate to better cosmological measurements
   - Mention how this reduces the need for manual data cleaning

## Implementation Notes

When enhancing this slide:

1. Maintain consistent formatting with the rest of the presentation
2. Ensure the mathematical notation matches that used in earlier slides
3. If possible, use actual data from your research for the image
4. Consider adding a brief animation that shows the before/after effect of applying anomaly detection

This enhanced slide serves as a crucial bridge between the mathematical framework of anomaly detection and the practical results in supernovae analysis, making the connection between SALT parameters and the anomaly detection method explicit and clear.