# JAX-bandflux Presentation Improvements

This document contains detailed recommendations for improving your "Bayesian Anomaly Detection for 1a supernovae using JAX-bandflux" presentation. The focus is on strengthening the connection between the SALT model parameters and the Bayesian anomaly detection framework.

## Table of Contents
1. [New Transition Slide](#new-transition-slide)
2. [Enhanced SALT Model Explanation](#enhanced-salt-model-explanation)
3. [Anomalous Measurements in SALT Fitting](#anomalous-measurements-in-salt-fitting)
4. [Strengthened Conclusion](#strengthened-conclusion)
5. [Additional Recommendations](#additional-recommendations)
6. [Bibliography and References](#bibliography-and-references)

## New Transition Slide

Add this slide after the "Key Implementation Details" slide (slide 188) and before the "Bayesian anomaly detection" section:

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

## Enhanced SALT Model Explanation

Replace the current "SALT Model in JAX-bandflux" slide (slide 136) with this enhanced version:

```latex
\begin{frame}{SALT Model in JAX-bandflux}
  \begin{itemize}
    \item SALT (Spectral Adaptive Lightcurve Template) model:
  \end{itemize}
  
  \begin{equation}
    F(p, \lambda) = x_0 \left[ M_0(p, \lambda) + x_1 M_1(p, \lambda) + \ldots \right] \times \exp \left[ c \times CL(\lambda) \right]
  \end{equation}
  
  \begin{itemize}
    \item Free parameters:
      \begin{itemize}
        \item $x_0$: Overall amplitude/normalization
        \item $x_1$: Stretch parameter (related to light curve width)
        \item $t_0$: Time of peak brightness
        \item $c$: Color parameter
      \end{itemize}
    \item Model surface parameters:
      \begin{itemize}
        \item $M_0(p, \lambda)$, $M_1(p, \lambda)$: Underlying flux surfaces
        \item $p$: Function of redshift and phase ($t-t_0$)
        \item $CL(\lambda)$: Color law function
      \end{itemize}
    \item \textbf{Challenge}: Anomalous measurements can bias parameter estimation
    \item \textbf{Solution}: Bayesian anomaly detection framework
  \end{itemize}
\end{frame}
```

## Anomalous Measurements in SALT Fitting

Enhance the "Anomalous measurements in SALT fitting" slide (slide 617) with this content:

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

## Strengthened Conclusion

Replace the current conclusion slide (slide 741) with this enhanced version:

```latex
\begin{frame}{Conclusions}
  \begin{itemize}
    \item JAX-bandflux enables GPU-accelerated supernova analysis
      \begin{itemize}
        \item Differentiable implementation of SALT model
        \item Efficient processing of large datasets
        \item Compatible with modern optimization techniques
      \end{itemize}
    \item Bayesian anomaly detection improves SALT parameter estimation
      \begin{itemize}
        \item More robust $x_0$, $x_1$, $t_0$, and $c$ estimates
        \item Automatically identifies and downweights outliers
        \item Flags problematic bandpasses
        \item Maximizes use of available data
      \end{itemize}
    \item Combined approach offers new possibilities for 1a supernovae cosmology
      \begin{itemize}
        \item More robust distance measurements
        \item Reduced systematic errors
        \item Potential for improved cosmological constraints
      \end{itemize}
    \item Open-source implementation available for community use
  \end{itemize}
\end{frame}
```

## Additional Recommendations

### 1. Add a Transition from Anomaly Detection to Results

Add this slide before the "Results on 1a supernovae" section (before slide 571):

```latex
\begin{frame}{From Theory to Application: Supernovae Analysis}
  \begin{itemize}
    \item Type Ia supernovae present unique challenges for data analysis:
      \begin{itemize}
        \item Instrumental artifacts in observations
        \item Atmospheric effects
        \item Host galaxy contamination
        \item Calibration errors
      \end{itemize}
    \item Traditional approaches:
      \begin{itemize}
        \item Manual inspection and removal of outliers
        \item Sigma-clipping algorithms
        \item Exclusion of entire problematic bandpasses
      \end{itemize}
    \item Our approach:
      \begin{itemize}
        \item Probabilistic treatment of anomalies
        \item Automatic identification during parameter inference
        \item Preservation of good data even from problematic bandpasses
      \end{itemize}
    \item JAX-bandflux + Bayesian anomaly detection = Robust parameter estimation
  \end{itemize}
\end{frame}
```

### 2. Enhance "What is anomaly detection useful for?" Slide

Modify slide 343 to include specific examples related to supernovae:

```latex
\begin{frame}{What is anomaly detection useful for?}
  \begin{columns}
    \begin{column}{0.5\textwidth}
        \textbf{1. Contamination}
        \begin{itemize}
          \item Simultaneously detecting and mitigating contaminated data
          \item In supernovae: Host galaxy contamination, instrumental artifacts
        \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
        \textbf{2. Anomalies}
        \begin{itemize}
          \item Radio transients, cosmic ray flares, GW signals
          \item In supernovae: Peculiar subtypes, calibration errors
        \end{itemize}
    \end{column}
  \end{columns}
\end{frame}
```

### 3. Add a Slide Showing Parameter Estimation Improvement

Add this slide in the Results section:

```latex
\begin{frame}{Improved Parameter Estimation}
  \begin{columns}
    \begin{column}{0.5\textwidth}
      \textbf{Traditional $\chi^2$ Fitting:}
      \begin{itemize}
        \item Sensitive to outliers
        \item Parameter biases from anomalous data
        \item Larger uncertainties in $x_0$, $x_1$, $t_0$, $c$
        \item Often requires manual data cleaning
      \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
      \textbf{Anomaly-Aware Fitting:}
      \begin{itemize}
        \item Robust against outliers
        \item Unbiased parameter estimation
        \item Reduced uncertainties
        \item Fully automated process
      \end{itemize}
    \end{column}
  \end{columns}
  
  \vspace{0.5cm}
  \centering
  [TABLE: Comparison of parameter uncertainties with and without anomaly detection]
\end{frame}
```

### 4. Replace Placeholder Images

For the slide "Why is it harder to write code for GPUs" (slide 65), replace the placeholder with an actual image showing the difference between CPU and GPU operations. You can use a diagram that shows:
- CPU: Few cores with complex operations
- GPU: Many simple cores for parallel operations

## Bibliography and References

Ensure the following references are included in your ref.bib file:

```bibtex
@article{jax2018github,
  title = {JAX: composable transformations of {P}ython+{N}um{P}y programs},
  author = {James Bradbury and Roy Frostig and Peter Hawkins and Matthew James Johnson and Chris Leary and Dougal Maclaurin and George Necula and Adam Paszke and Jake Vander{P}las and Skye Wanderman-{M}ilne and Qiao Zhang},
  year = {2018},
  url = {http://github.com/google/jax},
}

@article{kenworthy2021salt3,
  title={SALT3: An Improved Type Ia Supernova Model},
  author={Kenworthy, W. D. and Scolnic, D. and Riess, A. and others},
  journal={The Astrophysical Journal},
  volume={923},
  number={2},
  pages={265},
  year={2021},
  publisher={IOP Publishing}
}

@article{pierel2022salt3,
  title={SALT3-NIR: Extending Type Ia Supernova SALT Models to the Near-Infrared},
  author={Pierel, J. D. R. and Kenworthy, W. D. and Scolnic, D. and others},
  journal={arXiv preprint arXiv:2209.05594},
  year={2022}
}
```

Make sure to cite these references in the appropriate places in your presentation.

## Implementation Order

I recommend implementing these changes in the following order:

1. Add the transition slide between sections 1 and 2
2. Enhance the SALT model explanation in section 1
3. Modify the anomaly detection slides to reference SALT parameters
4. Add the transition slide before the Results section
5. Strengthen the results section to show impact on parameter estimation
6. Enhance the conclusion
7. Verify all references and citations
8. Replace placeholder images

This order ensures that the narrative flow is maintained throughout the implementation process.