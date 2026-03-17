# Machine Learning for Experimental Design Optimisation

## Talk Details
- **Date:** Thursday 19th March 2026, 14:15–14:35
- **Length:** 15 minutes presentation + 5 minutes questions
- **Conference:** AI in Radio Astronomy Workshop, Royal Observatory Edinburgh

## Abstract (as submitted)
Conditional Neural Bayes Ratio Estimation for Experimental Design Optimisation. Modern experiments spend millions or billions on buying new components (e.g. new antenna dishes for SKA). We propose a machine learning based method for automatic instrumental design optimisation, offering major cost savings and sensitivity gains. We give the example of simple antenna orientation in REACH leading to a ~20 percentage point sensitivity improvement forecast over a single night.

## Paper Abstract (Leeney et al.)
For frontier experiments operating at the edge of detectability, instrument design directly determines the probability of discovery. We introduce Conditional Neural Bayes Ratio Estimation (cNBRE), which extends neural ratio estimation by conditioning on design parameters, enabling a single trained network to estimate Bayes factors across a continuous design space. Applied to 21-cm radio cosmology with simulations representative of the REACH experiment, the amortised nature of cNBRE enables systematic design space exploration that would be intractable with traditional point-wise methods, while recovering established physical relationships. The analysis demonstrates a ~20 percentage point variation in detection probability with antenna orientation, a design decision that would be trivial to implement if determined prior to antenna construction. This framework enables efficient, globally-informed experimental design optimisation for a wide range of scientific applications.

## Talk Requirements
- Align with one or more core themes:
  1. **Scientific drivers for AI in radio astronomy** — How AI/ML enables or transforms SKA and pathfinder science
  2. **Technical enablers for AI adoption** — Infrastructure, platforms, software, workflows, and skills required to deploy AI at scale
  3. **Policy requirements for responsible and effective AI use** — FAIR and reproducible practices, transparency, sustainability, governance
- Append a short summary slide (templates: `summary_ai_radio_astronomy_2026.pptx` / `.key`)
- Upload by end of Tuesday 17th March
- Sessions will be recorded for internal UKRI DRI report

## Related Talks (Cambridge)
- **Eloy de Lera Acedo** — "AI/ML-Enabled Data-Intensive Radio Cosmology at Cavendish/Cambridge (REACH, SKA-LOW)" — Thu 13:55
- **Jacob Tutt** — "LLM-Era Compute for 21-cm Cosmology: JAX-Accelerated Bayesian & Simulation-Based Inference" — Thu 11:35
- **Harry Bevins** — "Instrument-Aware Error Bounds for Neural Network Emulators in Cosmology" — Thu 10:05
